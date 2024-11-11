<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {

      store: useStore(),

      guard_username: null,
      guard_password: null,
      guard_entrances: [],

      user_for_delete: null,

    };
  },

  async mounted() {
    await this.store.getEntrances();
    await this.store.getUsers();
  },

  computed: {
    // Computed property to filter users with the "inhabitant" role
    guards() {
      return this.store.users.filter(user => user.role === "guard");
    },
  },

  methods: {

    async submitGuardForm() {

      const guard = {
        username: this.guard_username,
        password: this.guard_password,
        entrances: this.guard_entrances,
      };

      try {
        await axios.post("http://localhost:8000/backend/api/add_guard/", guard, {
          headers: {
            "Content-Type": "application/json",
          },
        });

      this.store.getUsers();
      } catch (error) {
        console.error("Error creating guard:", error);
        alert("Failed to create guard.");
      }
    },

    async deleteUser() {
    try {
      const response = await axios.delete(`http://localhost:8000/backend/api/delete_user/${this.user_for_delete}/`, {
        headers: {
          "Content-Type": "application/json",
        },
      });
      this.store.getUsers();
    } catch (error) {
      console.error("Error deleting user:", error);
      alert("Failed to delete user.");
    }
  },
  },
};
</script>

<template>

<div class="manage-users">

  <h1>Manage Guard</h1>

  <div class="create-guard-page">
    <h2>Create Guard</h2>
    <form @submit.prevent="submitGuardForm" class="guard-form">
      <!-- Username Field -->
      <div class="form-group">
        <label for="username">Username:</label><br>
        <input v-model="this.guard_username" type="text" id="guard_username" required />
      </div>

      <!-- Password Field -->
      <div class="form-group">
        <label for="password">Password:</label><br>
        <input v-model="this.guard_password" type="password" id="guard_password" required />
      </div>

      <!-- Buildings Multi-Select Dropdown -->
      <div class="form-group">
        <label for="entrances">Entrances:</label><br>
        <select v-model="this.guard_entrances" id="guard_entrances" multiple>
          <option v-for="entrance in this.store.entrances" :key="entrance.id" :value="entrance.id">
            {{ entrance.building }} - {{ entrance.number }}
          </option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Add Guard</button>
    </form>
  </div>

  <div class="delete-user">
    <h2>Guard Deleting</h2>

    <ul>
      <label for="userSelect">Select Guard:</label><br>
      <select v-model="this.user_for_delete" id="userSelect">
        <option disabled value="">Select a User</option>
        <option v-for="user in guards" :key="user.id" :value="user.id">
          {{ user.username }} - {{ user.role }}
        </option>
      </select>    
    </ul>

    <button @click="deleteUser" class="btn btn-danger" :disabled="!this.user_for_delete">
      Delete User
    </button>
  </div>
</div>

</template>