import { createApp } from "vue";
import { createPinia } from "pinia";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/main.css";
import App from "./App.vue";
import { useStore } from "./stores/store.js";

const app = createApp(App);

app.use(createPinia());
app.use(router);

const store = useStore();
store.setCsrfToken();

app.mount("#app");
