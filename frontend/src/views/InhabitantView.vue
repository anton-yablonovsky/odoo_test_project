<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {

      store: useStore(),

      inhabitant_username: null,
      inhabitant_password: null,
      inhabitant_apartments: [],

      user_for_delete: null,

    };
  },

  async mounted() {
    await this.store.getApartments();
    await this.store.getUsers();
  },

  computed: {
    // Computed property to filter users with the "inhabitant" role
    inhabitants() {
      return this.store.users.filter(user => user.role === "inhabitant");
    },
  },

  methods: {

    async submitInhabitantForm() {

      const inhabitant = {
        username: this.inhabitant_username,
        password: this.inhabitant_password,
        apartments: this.inhabitant_apartments,
      };

      try {
        await axios.post("http://localhost:8000/backend/api/add_inhabitant/", inhabitant, {
          headers: {
            "Content-Type": "application/json",
          },
        });

      this.store.getUsers();
      } catch (error) {
        console.error("Error creating inhabitant:", error);
        alert("Failed to create inhabitant.");
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

  <h1>Manage Inhabitant</h1>

  <div class="create-inhabitant-page">
    <h2>Create Inhabitant</h2>
    <form @submit.prevent="submitInhabitantForm" class="inhabitant-form">
      <!-- Username Field -->
      <div class="form-group">
        <label for="username">Username:</label><br>
        <input v-model="this.inhabitant_username" type="text" id="inhabitant_username" required />
      </div>

      <!-- Password Field -->
      <div class="form-group">
        <label for="password">Password:</label><br>
        <input v-model="this.inhabitant_password" type="password" id="inhabitant_password" required />
      </div>

      <!-- Buildings Multi-Select Dropdown -->
      <div class="form-group">
        <label for="apartments">Apartments:</label><br>
        <select v-model="this.inhabitant_apartments" id="inhabitant_apartments" multiple>
          <option v-for="apartment in this.store.apartments" :key="apartment.id" :value="apartment.id">
            {{ apartment.entrance }} - {{ apartment.number }}
          </option>
        </select>
      </div>

      <!-- Submit Button -->
      <button type="submit" class="btn btn-primary">Add Inhabitant</button>
    </form>
  </div>

  <div class="delete-user">
    <h2>Inhabitant Deleting</h2>

    <ul>
      <label for="userSelect">Select Inhabitant</label><br>
      <select v-model="this.user_for_delete" id="userSelect">
        <option disabled value="">Select a User</option>
        <option v-for="user in inhabitants" :key="user.id" :value="user.id">
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