<template>
  <div class="row justify-center">
    <div class="col-6">
      <q-card>
        <q-card-section class="text-center">
          <q-btn-dropdown
            no-caps
            flat
            :label="timespan.label"
            v-model="timespanMenu"
            style="margin-bottom:2.20px"
          >
            <q-list>
              <q-item
                clickable
                v-close-popup
                no-caps
                @click="timespan.label = 'For the last 2 hours'; timespan.value = 7200; getClientTraffic()"
              >
                <q-item-section>
                  <q-item-label>For the last 2 hours</q-item-label>
                </q-item-section>
              </q-item>
              <q-item
                clickable
                v-close-popup
                no-caps
                @click="timespan.label = 'For the last day'; timespan.value = 86400; getClientTraffic()"
              >
                <q-item-section>
                  <q-item-label>For the last day</q-item-label>
                </q-item-section>
              </q-item>
              <q-item
                clickable
                v-close-popup
                no-caps
                @click="timespan.label = 'For the last week'; timespan.value = 604800; getClientTraffic()"
              >
                <q-item-section>
                  <q-item-label>For the last week</q-item-label>
                </q-item-section>
              </q-item>
              <q-item
                clickable
                v-close-popup
                @click="timespan.label = 'For the last 30 days'; timespan.value = 2592000; getClientTraffic()"
              >
                <q-item-section>
                  <q-item-label>For the last 30 days</q-item-label>
                </q-item-section>
              </q-item>
              <q-item clickable>
                <q-item-section v-ripple>
                  <q-item-label>Custom range</q-item-label>
                  <q-popup-proxy
                    @before-show="updateProxy"
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-date v-model="dateRange" :options="dateOptions" range>
                      <div class="row items-center justify-end q-gutter-sm">
                        <q-btn label="Cancel" color="primary" flat v-close-popup />
                        <q-btn
                          label="OK"
                          color="primary"
                          flat
                          @click="timespan.value = dateRange; timespanMenu = false; getClientTraffic()"
                          v-close-popup
                        />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-item-section>
              </q-item>
            </q-list>
          </q-btn-dropdown>
          <div>
            <span class="text-h6">{{ totalUsage }}</span>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
  <div class="row justify-center q-my-sm">
    <div class="col-3 q-pr-sm">
      <q-card>
        <q-card-section class="text-center">
          <span class="text-weight-light">Downloaded</span>
          <div class="text-h6">{{ totalRecv }}</div>
        </q-card-section>
      </q-card>
    </div>
    <div class="col-3">
      <q-card>
        <q-card-section class="text-center">
          <span class="text-weight-light">Uploaded</span>
          <div class="text-h6">{{ totalSent }}</div>
        </q-card-section>
      </q-card>
    </div>
  </div>
  <q-table
    :rows="rows"
    :columns="columns"
    row-key="id"
    :pagination="pagination"
    :loading="tableLoading"
    :filter="filter"
    :visible-columns="visibleColumns"
  >
    <template v-slot:top-left>
      <div>
        <q-btn
          flat
          dense
          @click="timespan.label = 'For the last 2 hours'; timespan.value = 7200; getClientTraffic()"
          icon="refresh"
          label="Client Traffic"
          class="q-mr-md"
        />
      </div>
    </template>
    <template v-slot:top-right>
      <div>
        <q-input outlined clearable dense debounce="300" v-model="filter" label="Search">
          <template v-slot:prepend>
            <q-icon name="search" />
          </template>
        </q-input>
      </div>
    </template>
    <template v-slot:body="props">
      <q-tr :props="props">
        <q-td key="status" :props="props">
          <q-icon v-if="props.row.status == 'Online'" name="brightness_1" color="positive" />
          <q-icon v-else name="brightness_1" color="negative" />
        </q-td>
        <q-td key="id" :props="props">
          <q-btn
            flat
            no-caps
            class="text-weight-bold q-px-none"
            @click="getDevicePolicy(props.row)"
          >{{ props.row.id }}</q-btn>
        </q-td>

        <q-td key="user" :props="props">{{ props.row.user }}</q-td>
        <q-td key="description" :props="props">{{ props.row.description }}</q-td>
        <q-td key="ip" :props="props">{{ props.row.ip }}</q-td>
        <q-td key="mac" :props="props">{{ props.row.mac }}</q-td>
        <q-td key="usageTotal" :props="props">{{ props.row.usage.total }}</q-td>
        <q-td key="totalUsage" :props="props">{{ props.row.usage.total }}</q-td>
        <q-td key="firstSeen" :props="props">{{ props.row.firstSeen }}</q-td>
        <q-td key="lastSeen" :props="props">{{ props.row.lastSeen }}</q-td>
        <q-td key="os" :props="props">{{ props.row.os }}</q-td>
        <q-td key="vlan" :props="props">{{ props.row.vlan }}</q-td>
        <q-td key="recentDeviceName" :props="props">{{ props.row.recentDeviceName }}</q-td>
        <q-td key="recentDeviceMac" :props="props">{{ props.row.recentDeviceMac }}</q-td>
        <q-td key="recentDeviceSerial" :props="props">{{ props.row.recentDeviceSerial }}</q-td>
      </q-tr>
    </template>
  </q-table>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useQuasar, date } from "quasar";
import Policy from "@/components/integrations/meraki/modals/Policy";

const columns = [
  {
    name: "status",
    label: "Status",
    align: "left",
    field: (row) => row.status,
    format: (val) => `${val}`,
    sortable: true,
  },
  {
    name: "id",
    align: "left",
    label: "ID",
    field: "id",
    sortable: true,
  },
  {
    name: "user",
    align: "left",
    label: "User",
    field: "user",
    sortable: true,
  },
  {
    name: "description",
    align: "left",
    label: "Description",
    field: "description",
    sortable: true,
  },
  {
    name: "ip",
    label: "IPv4",
    field: "ip",
    align: "left",
    sortable: true,
  },
  {
    name: "usageTotal",
    label: "Usage",
    field: "usageTotal",
    align: "left",
    sortable: false,
  },
  {
    name: "totalUsage",
    label: "Total Usage",
    field: "totalUsage",
    align: "left",
    field: (row) => row.totalUsage,
    format: (val) => `${val}`,
    sortable: true
  },
  {
    name: "firstSeen",
    label: "First Seen",
    field: "firstSeen",
    align: "left",
    sortable: true,
  },
  {
    name: "lastSeen",
    label: "Last Seen",
    field: "lastSeen",
    align: "left",
    sortable: true,
  },
  {
    name: "os",
    label: "OS",
    field: "os",
    align: "left",
    sortable: true,
  },
  {
    name: "vlan",
    label: "VLAN",
    field: "vlan",
    align: "left",
    sortable: true,
  },
  {
    name: "recentDeviceName",
    label: "Recent Device Name",
    field: "recentDeviceName",
    align: "left",
    sortable: true,
  },
  {
    name: "recentDeviceMac",
    label: "Recent Device MAC",
    field: "recentDeviceMac",
    align: "left",
    sortable: true,
  },
  {
    name: "recentDeviceSerial",
    label: "Recent Device Serial",
    field: "recentDeviceSerial",
    align: "left",
    sortable: true,
  }
];

export default {
  name: "NetworkClientsTrafficTable",
  props: ["organizationID", "organizationName", "networkID", "networkName"],

  setup(props) {
    const $q = useQuasar();

    const timespanMenu = ref(false)
    const timespan = ref({ label: "For the last 2 hours", value: 7200 })
    const rows = ref([])
    const totalUsage = ref(null)
    const totalRecv = ref(null)
    const totalSent = ref(null)
    const filter = ref("")
    const dateOptions = ref([])
    const dateRange = ref("")
    const updateProxy = ref("")
    const tableLoading = ref(false)

    function formatUsage(usage) {
      if (usage < 1024) {
        let totalKB = usage.toFixed(0)
        return String(totalKB) + " KB"

      } else if (usage / 1024 < 1024) {
        let totalMB = (usage / 1024).toFixed(2)
        return String(totalMB) + " MB"

      } else if (usage / 1024 / 1024 < 1024) {
        let totalGB = (usage / 1024 / 1024).toFixed(2)
        return String(totalGB) + " GB"

      } else if (usage / 1024 / 1024 / 1024 < 1024) {
        let totalTB = (usage / 1024 / 1024 / 1024).toFixed(2)
        return String(totalTB) + " TB"

      }
    }

    function getClientTraffic() {
      tableLoading.value = true

      for (let i = 0; i < 31; i++) {
        let newDate = date.subtractFromDate(new Date(), { days: i });
        let formattedDate = date.formatDate(newDate, "YYYY/MM/DD");
        dateOptions.value.push(formattedDate);
      }

      if (typeof timespan.value.value === 'object') {
        const t0 = date.formatDate(timespan.value.value.from, "YYYY-MM-DDT00:00:00.000Z");
        const t1 = date.formatDate(timespan.value.value.to, "YYYY-MM-DDT23:59:00.000Z");
        timespan.value.value = "t0=" + t0 + "&t1=" + t1
        timespan.value.label = date.formatDate(t0, "MMM D, YYYY @ hh:mm A") + " - " + date.formatDate(t1, "MMM D, YYYY @ hh:mm A")

      } else if (timespan.value.value !== 7200 && timespan.value.value !== 86400 && timespan.value.value !== 604800 && timespan.value.value !== 2592000) {
        const t0 = date.formatDate(timespan.value.value, "YYYY-MM-DDT00:00:00.000Z");
        const t1 = date.formatDate(timespan.value.value, "YYYY-MM-DDT23:59:00.000Z");
        timespan.value.value = "t0=" + t0 + "&t1=" + t1
        timespan.value.label = date.formatDate(t0, "MMM D, YYYY @ hh:mm A") + " - " + date.formatDate(t1, "MMM D, YYYY @ hh:mm A")
      }

      axios
        .get(`/meraki/` + props.networkID + `/clients/traffic/` + timespan.value.value + `/`)
        .then(r => {
          console.log(r.data)
          rows.value = []
          totalUsage.value = 0
          totalRecv.value = 0
          totalSent.value = 0

          for (let client of r.data) {
            let returnedUsage = formatUsage(client.usage.total)
            totalUsage.value += client.usage.total
            totalRecv.value += client.usage.recv
            totalSent.value += client.usage.sent

            let clientObj = {
              status: client.status,
              id: client.id,
              name: client.name,
              user: client.user,
              description: client.description,
              mac: client.mac,
              ip: client.ip,
              mac: client.mac,
              usage: { total: returnedUsage, recv: client.usage.recv, sent: client.usage.sent },
              totalUsage: client.usage.recv + client.usage.sent,
              recentDeviceMac: client.recentDeviceMac,
              recentDeviceName: client.recentDeviceName,
              recentDeviceSerial: client.recentDeviceSerial,
              firstSeen: date.formatDate(client.firstSeen, "MMM DD, YYYY @ h:mm A"),
              lastSeen: date.formatDate(client.lastSeen, "MMM DD, YYYY @ h:mm A"),
              os: client.os,
              vlan: client.vlan
            }
            rows.value.push(clientObj)
          }
          let returnedTotalUsage = formatUsage(totalUsage.value)
          let returnedTotalRecv = formatUsage(totalRecv.value)
          let returnedTotalSent = formatUsage(totalSent.value)

          totalUsage.value = returnedTotalUsage
          totalRecv.value = returnedTotalRecv
          totalSent.value = returnedTotalSent
          tableLoading.value = false
        })
        .catch(e => {

        });
    }

    function getDevicePolicy(client) {
      $q.dialog({
        component: Policy,
        componentProps: {
          networkId: props.networkID,
          client: client
        }
      })
    }

    onMounted(() => {
      getClientTraffic();
    })

    return {
      pagination: {
        sortBy: 'totalUsage',
        descending: true,
        page: 1,
        rowsPerPage: 10
      },
      visibleColumns: ref(['status', 'id', 'user', 'description', 'ip', 'usageTotal', 'firstSeen', 'lastSeen', 'recentDeviceName', 'recentDeviceMac', 'recentDeviceSerial', 'os', 'vlan']),
      timespanMenu,
      timespan,
      columns,
      rows,
      totalUsage,
      totalRecv,
      totalSent,
      filter,
      dateOptions,
      dateRange,
      updateProxy,
      tableLoading,
      getClientTraffic,
      getDevicePolicy
    };
  }
}
</script>