<script>
import axios from "axios";
import router from "../router";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
      username: "",
      password: "",
    };
  },

  async mounted() {

  },

  methods: {
    async submitForm(e) {
      await this.store.login(this.username, this.password)

      if (this.store.isAuthenticatedState) {

        await this.store.getUserRole();

        router.push("/");
        
      } 

      else {
        router.push("/login");
        alert("Access denied!");
      }
    },
  },
};
</script>

<template>
  <div class="log-in-page">
    <div class="login-form">
      <h1 class="login-text">Please login</h1>
      <form @submit.prevent="submitForm" class="login-form-body">
        <div class="login-form-input-group">
          <label class="form-label login-form-input-label">Username</label>
          <input
            type="username"
            class="form-control login-form-input"
            v-model="username"
          />
        </div>
        <div class="login-form-input-group">
          <label class="form-label login-form-input-label">Password</label>
          <input
            type="password"
            class="form-control login-form-input"
            v-model="password"
          />
        </div>
        <p class="login-form-text">
          Enter Name and Password then press "ENTER"
        </p>
        <button class="btn btn-primary login-form-submit">ENTER</button>
      </form>
    </div>
  </div>
</template>
