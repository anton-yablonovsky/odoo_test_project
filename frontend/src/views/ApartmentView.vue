<script>
import axios from "axios";
import { useStore } from "../stores/store.js";
import router from "../router";

export default {
  data() {
    return {
      store: useStore(),

      apartment_entrance: null,
      apartment_number: null,
      apartment_for_delete: null,
    };
  },

  async mounted() {
    await this.store.getApartments();
  },

  methods: {
    async submitApartmentForm() {
      const formData = {
        entrance: this.apartment_entrance,
        number: this.apartment_number,
      };

      try {
        await axios.post(
          "http://localhost:8000/backend/api/add_apartment/",
          formData,
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );

        await this.store.getApartments();
      } catch (error) {
        console.error("Error creating apartment:", error);
        alert("Failed to create apartment.");
      }
    },

    async deleteApartmentForm() {
      if (!this.apartment_for_delete) {
        alert("Please select an apartment to delete.");
        return;
      }

      try {
        await axios.delete(
          `http://localhost:8000/backend/api/delete_apartment/${this.apartment_for_delete}/`,
          {
            headers: {
              "Content-Type": "application/json",
            },
          },
        );

        await this.store.getApartments();
      } catch (error) {
        console.error("Error deleting apartment:", error);
        alert("Failed to delete apartment.");
      }
    },
  },
};
</script>

<template>
  <div class="manage-apartments">
    <h1>Manage Apartments</h1>

    <div class="create-apartment-page">
      <h2>Create Apartment</h2>
      <form @submit.prevent="submitApartmentForm" class="apartment-form">
        <!-- Building Dropdown -->
        <div class="form-group">
          <label for="apartment">Apartment Entrance:</label><br />
          <select
            v-model="this.apartment_entrance"
            id="apartment_entrance"
            required
          >
            <option value="" disabled>Select an Entrance</option>
            <option
              v-for="entrance in this.store.entrances"
              :key="entrance.id"
              :value="entrance.id"
            >
              {{ entrance.building }} - {{ entrance.number }}
            </option>
          </select>
        </div>

        <!-- Entrance Number Field -->
        <div class="form-group">
          <label for="number">Apartment Number:</label><br />
          <input
            v-model="this.apartment_number"
            type="text"
            id="apartment_number"
            required
          />
        </div>

        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary">Add Apartment</button>
      </form>
    </div>

    <div>
      <h2>Delete an Appartment</h2>
      <form @submit.prevent="deleteApartmentForm" class="delete-apartment-form">
        <div class="form-group">
          <label for="apartmentSelect">Select Apartment to Delete:</label><br />
          <select
            v-model="this.apartment_for_delete"
            id="apartment_for_delete"
            required
          >
            <option value="" disabled>Select an Apartment</option>
            <option
              v-for="apartment in this.store.apartments"
              :key="apartment.id"
              :value="apartment.id"
            >
              {{ apartment.entrance }} - {{ apartment.number }}
            </option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Delete Apartment</button>
      </form>
    </div>
  </div>
</template>
