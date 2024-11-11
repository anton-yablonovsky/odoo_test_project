import { createRouter, createWebHistory } from "vue-router";
import AdditionalLayout from "../layouts/AdditionalLayout.vue";
import MainLayout from "../layouts/MainLayout.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [

    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
      meta: {
        layout: AdditionalLayout,
      },
    },

    {
      path: "/",
      name: "main",
      component: () => import("../views/MainView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/inhabitant",
      name: "inhabitant",
      component: () => import("../views/InhabitantView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/guard",
      name: "guard",
      component: () => import("../views/GuardView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/manager",
      name: "manager",
      component: () => import("../views/ManagerView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/apartment",
      name: "apartment",
      component: () => import("../views/ApartmentView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/entrance",
      name: "entrance",
      component: () => import("../views/EntranceView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

    {
      path: "/building",
      name: "building",
      component: () => import("../views/BuildingView.vue"),
      meta: {
        layout: MainLayout,
      },
    },

  ],
});

export default router;
