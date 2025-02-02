const routes = [
  {
    path: "/",
    name: "MainLayout",
    component: () => import("@/layouts/MainLayout"),
    children: [
      {
        path: "agents/:agent_id",
        name: "Agent",
        component: () => import("@/views/Agent"),
        meta: {
          requireAuth: true
        }
      },
      {
        path: "",
        name: "Dashboard",
        component: () => import("@/views/Dashboard"),
        meta: {
          requireAuth: true
        }
      },
    ]
  },
  {
    path: "/setup",
    name: "InitialSetup",
    component: () => import("@/views/InitialSetup"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/totp_setup",
    name: "TOTPSetup",
    component: () => import("@/views/TOTPSetup"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/takecontrol/:agent_id",
    name: "TakeControl",
    component: () => import("@/views/TakeControl"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/integrations/agents/:agent_id",
    name: "AgentIntegrations",
    component: () => import("@/views/AgentIntegrations"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/integrations/clients/:client_id",
    name: "ClientIntegrations",
    component: () => import("@/views/ClientIntegrations"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/remotebackground/:agent_id",
    name: "RemoteBackground",
    component: () => import("@/views/RemoteBackground"),
    meta: {
      requireAuth: true
    }
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login"),
    meta: {
      requiresVisitor: true
    }
  },
  {
    path: "/expired",
    name: "SessionExpired",
    component: () => import("@/views/SessionExpired")
  },
  { path: "/:catchAll(.*)*", component: () => import("@/views/NotFound") }
]

export default routes
