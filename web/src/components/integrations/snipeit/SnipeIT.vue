<template>
    <q-card flat>
        <q-tabs
            v-model="tab"
            dense
            align="left"
            class="text-grey"
            active-color="primary"
            indicator-color="primary"
            no-caps
            narrow-indicator
            inline-label
        >
            <q-tab icon="computer" name="asset" label="Asset" />
            <q-tab icon="category" name="models" label="Models" />
            <q-tab icon="build" name="maintenances" label="Maintenances" />
        </q-tabs>
        <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="asset" class="q-px-none">
                <q-btn-dropdown label="Actions" flat>
                    <q-list>
                        <q-item clickable v-close-popup @click="checkout()">
                            <q-item-section>
                                <q-item-label>Checkout</q-item-label>
                            </q-item-section>
                        </q-item>
                        <q-item clickable v-close-popup @click="checkin()">
                            <q-item-section>
                                <q-item-label>Checkin</q-item-label>
                            </q-item-section>
                        </q-item>
                        <q-item clickable v-close-popup @click="addMaintenance()">
                            <q-item-section>
                                <q-item-label>Add Maintenance</q-item-label>
                            </q-item-section>
                        </q-item>
                        <q-separator />
                        <q-item clickable v-close-popup @click="editAsset()">
                            <q-item-section>
                                <q-item-label>Edit Asset</q-item-label>
                            </q-item-section>
                        </q-item>
                        <q-item clickable v-close-popup @click="deleteAsset()">
                            <q-item-section>
                                <q-item-label>Delete Asset</q-item-label>
                            </q-item-section>
                        </q-item>
                    </q-list>
                </q-btn-dropdown>
                <div class="row">
                    <div class="col-5">
                        <q-list>
                            <q-item-section>
                                <q-item-label header>GENERAL</q-item-label>
                            </q-item-section>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Name</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.name }}</q-item-section>
                            </q-item>
                            <q-item dense v-if="asset.status_label">
                                <q-item-section top>
                                    <q-item-label>Status</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.status_label.name }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Asset Tag</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.asset_tag }}</q-item-section>
                            </q-item>
                            <q-item dense v-if="asset.model">
                                <q-item-section top>
                                    <q-item-label>Model Name</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.model.name }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Model Number</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.model_number }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Serial</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.serial }}</q-item-section>
                            </q-item>
                            <q-item dense v-if="asset.company">
                                <q-item-section top>
                                    <q-item-label>Company</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.company.name }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Location</q-item-label>
                                </q-item-section>
                                <q-item-section
                                    side
                                    top
                                    v-if="asset.location"
                                >{{ asset.location.name }}</q-item-section>
                            </q-item>
                            <q-separator inset />
                            <q-item-label header>PURCHASING</q-item-label>
                            <q-item dense v-if="asset.manufacturer">
                                <q-item-section top>
                                    <q-item-label>Manufacturer</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.manufacturer.name }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Purchase Date</q-item-label>
                                </q-item-section>
                                <q-item-section
                                    side
                                    top
                                    v-if="asset.purchase_date"
                                >{{ asset.purchase_date.formatted }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Purchase Cost</q-item-label>
                                </q-item-section>
                                <q-item-section side top>${{ asset.purchase_cost }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Order Number</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.order_number }}</q-item-section>
                            </q-item>
                            <q-separator inset />
                            <q-item-label header>WARRANTY</q-item-label>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Months</q-item-label>
                                </q-item-section>
                                <q-item-section side top>{{ asset.warranty_months }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>Expires</q-item-label>
                                </q-item-section>
                                <q-item-section
                                    side
                                    top
                                    v-if="asset.warranty_expires"
                                >{{ asset.warranty_expires.formatted }}</q-item-section>
                            </q-item>
                            <q-item dense>
                                <q-item-section top>
                                    <q-item-label>End of Life</q-item-label>
                                </q-item-section>
                                <q-item-section side top v-if="asset.eol">{{ asset.eol.formatted }}</q-item-section>
                            </q-item>
                        </q-list>
                    </div>
                    <div class="col-7">
                        <div class="row q-mt-sm">
                            <div class="col-12">
                                <q-card class="q-mx-sm q-mb-sm">
                                    <q-card-section class="text-center" v-if="!asset.assigned_to">
                                        <span class="text-weight-light">Checked In To</span>
                                        <div
                                            class="text-h6"
                                            v-if="asset.location"
                                        >{{ asset.location.name }}</div>
                                    </q-card-section>
                                    <q-card-section class="text-center" v-else>
                                        <span class="text-weight-light">Checked Out To</span>
                                        <div
                                            class="text-h6"
                                            v-if="asset.assigned_to"
                                        >{{ asset.assigned_to.name }}</div>
                                    </q-card-section>
                                </q-card>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12">
                                <q-card class="q-mx-sm q-mb-sm">
                                    <q-card-section class="text-center">
                                        <span class="text-weight-light">Current Value</span>
                                        <div class="text-h6">${{ currentValue }}</div>
                                    </q-card-section>
                                </q-card>
                            </div>
                            <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12">
                                <q-card class="q-mx-sm q-mb-sm">
                                    <q-card-section class="text-center">
                                        <span class="text-weight-light">Monthly Depcreciation</span>
                                        <div class="text-h6">${{ monthlyDepreciation }}</div>
                                    </q-card-section>
                                </q-card>
                            </div>
                            <div class="col-lg-4 col-md-6 col-sm-12 col-xs-12">
                                <q-card class="q-mx-sm q-mb-sm">
                                    <q-card-section class="text-center">
                                        <span class="text-weight-light">Difference</span>
                                        <div class="text-h6">${{ difference }}</div>
                                    </q-card-section>
                                </q-card>
                            </div>
                        </div>
                    </div>
                </div>
            </q-tab-panel>
            <q-tab-panel name="models" class="q-px-none">
                <ModelsTab />
            </q-tab-panel>
            <q-tab-panel name="maintenances" class="q-px-none">
                <MaintenancesTab :asset="asset" />
            </q-tab-panel>
        </q-tab-panels>
    </q-card>
</template>

<script>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useQuasar, useDialogPluginComponent, date } from "quasar";
import { notifyError } from "@/utils/notify";
import AssetForm from "@/components/integrations/snipeit/modals/AssetForm";
import Checkout from "@/components/integrations/snipeit/modals/Checkout";
import Checkin from "@/components/integrations/snipeit/modals/Checkin";
import AddMaintenance from "@/components/integrations/snipeit/modals/AddMaintenance";
import DeleteAsset from "@/components/integrations/snipeit/modals/DeleteAsset";
import ModelsTab from "@/components/integrations/snipeit/ModelsTab";
import MaintenancesTab from "@/components/integrations/snipeit/MaintenancesTab";

export default {
    name: "SnipeIT",
    emits: [...useDialogPluginComponent.emits],
    props: ['agent'],
    components: { ModelsTab, MaintenancesTab },

    setup(props) {
        const { dialogRef, onDialogHide, onDialogOK } = useDialogPluginComponent();
        const $q = useQuasar();

        const tab = ref("")
        const asset = ref([])
        const foundAsset = ref(null)
        const monthlyDepreciation = ref("")
        const currentValue = ref("")
        const difference = ref("")

        function getHardware() {
            $q.loading.show()
            axios
                .get(`/snipeit/hardware/`, { params: { status: 'All' } })
                .then(r => {
                    const tacticalAgentModels = []
                    const tacticalAgentHostname = []
                    const tacticalAgentSerial = []
                    const snipeITAssetsModelNameNumber = []
                    const snipeITAssetsModelNumber = []
                    const snipeITAssetTags = []
                    const snipeITAssetHostnames = []

                    tacticalAgentModels.push(props.agent.wmi_detail.comp_sys[0][0].Model)
                    tacticalAgentModels.push(props.agent.wmi_detail.comp_sys_prod[0][0].Name)
                    tacticalAgentHostname.push(props.agent.hostname)
                    tacticalAgentSerial.push(props.agent.wmi_detail.comp_sys_prod[0][0].IdentifyingNumber)
                    let i = 0;
                    do {
                        snipeITAssetsModelNameNumber.push(r.data.rows[i].model.name + " " + r.data.rows[i].model_number)
                        snipeITAssetsModelNumber.push(r.data.rows[i].model_number)
                        snipeITAssetTags.push(r.data.rows[i].asset_tag)
                        snipeITAssetHostnames.push(r.data.rows[i].name)

                        //Match on Model Number
                        const modelNumber = tacticalAgentModels.filter(element => snipeITAssetsModelNumber.includes(element))
                        //Match on Model Name and Number
                        const modelNameNumber = tacticalAgentModels.filter(element => snipeITAssetsModelNameNumber.includes(element))
                        //Match on Asset Tag
                        const assetTag = tacticalAgentModels.filter(element => snipeITAssetTags.includes(element))
                        //Match on hostname
                        const hostnameMatch = tacticalAgentHostname.filter(element => snipeITAssetHostnames.includes(element))
                        //Match on serial
                        const serial = tacticalAgentSerial.filter(element => snipeITAssetTags.includes(element))

                        if (modelNumber.length > 0 && hostnameMatch.length > 0 || modelNameNumber.length > 0 && hostnameMatch.length > 0 || modelNumber.length > 0 && modelNameNumber.length > 0 && hostnameMatch.length > 0 || assetTag.length > 0 && hostnameMatch.length > 0 || serial.length > 0 && hostnameMatch.length > 0) {
                            if (r.data.rows[i].eol && r.data.rows[i].purchase_date && r.data.rows[i].purchase_cost) {
                                const newDate = new Date()
                                const eolDate = r.data.rows[i].eol.date
                                const purchase_date = r.data.rows[i].purchase_date.date
                                const unit = 'months'

                                const depreciationDateDiff = date.getDateDiff(eolDate, purchase_date, unit)
                                const depreciationCost = parseInt(r.data.rows[i].purchase_cost.replace(/,/g, ''), 10) / depreciationDateDiff
                                const currentDepreciationValue = date.getDateDiff(newDate, purchase_date, unit)

                                currentValue.value = (parseInt(r.data.rows[i].purchase_cost.replace(/,/g, ''), 10) - (currentDepreciationValue * depreciationCost)).toFixed(2)
                                difference.value = (currentDepreciationValue * depreciationCost).toFixed(2)
                                monthlyDepreciation.value = depreciationCost.toFixed(2)
                            }
                            asset.value = []
                            asset.value = r.data.rows[i]
                            tab.value = 'asset'
                            foundAsset.value = true
                            $q.loading.hide()
                            return;
                        } else {
                            foundAsset.value = false
                        }
                        i++;
                    } while (i < r.data.rows.length);
                    $q.loading.hide()
                    notifyError("Could not find a " + props.agent.hostname + " asset with the same asset tag, hostname or model number in Snipe-IT")
                    addAsset()
                })
                .catch(e => {
                    console.log(e)
                });
        }

        function addAsset() {
            $q.dialog({
                component: AssetForm,
                componentProps: {
                    agent: props.agent,
                }
            }).onOk(() => {
                getHardware()
            })
        }

        function checkout() {
            $q.dialog({
                component: Checkout,
                componentProps: {
                    agent: props.agent,
                    asset: asset.value
                }
            }).onOk(() => {
                getHardware()
            })
        }

        function checkin() {
            $q.dialog({
                component: Checkin,
                componentProps: {
                    agent: props.agent,
                    asset: asset.value
                }
            }).onOk(() => {
                getHardware()
            })
        }

        function addMaintenance() {
            $q.dialog({
                component: AddMaintenance,
                componentProps: {
                    asset: asset.value
                }
            }).onOk(() => {
                tab.value = 'maintenances'
            })
        }

        function editAsset() {
            $q.dialog({
                component: AssetForm,
                componentProps: {
                    agent: props.agent,
                    asset: asset.value
                }
            }).onOk(() => {
                getHardware()
            })
        }

        function deleteAsset() {
            $q.dialog({
                component: DeleteAsset,
                componentProps: {
                    agent: props.agent,
                    asset: asset.value
                }
            }).onOk(() => {
                asset.value = []
            })
        }

        onMounted(() => {
            getHardware()
        });

        return {
            tab,
            asset,
            monthlyDepreciation,
            currentValue,
            difference,
            checkout,
            checkin,
            editAsset,
            deleteAsset,
            addMaintenance,
            // quasar dialog
            dialogRef,
            onDialogHide,
        };
    },
};
</script>