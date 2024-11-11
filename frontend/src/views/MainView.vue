<script>
import { useStore } from "../stores/store.js";
import axios from "axios";

export default {
  data() {
    return {
      store: useStore(),
      manager_building: null,
    };
  },
  methods: {

  },

  async mounted() {

    this.store.getApartments();
    this.store.getEntrances();
    this.store.getBuildings();
    this.store.getUserRole();

    if (this.store.userRole == "manager") {
      this.store.getManagerBuildings();
    }
    else if (this.store.userRole == "guard") {
      this.store.getGuardEntrances();
      console.log("this.store.guard_entrances");
      console.log(this.store.guard_entrances);
    }
    else if (this.store.userRole == "inhabitant") {
      this.store.getInhabitantApartments();
    }

  },

  computed: {
    adminBuildings() {
      return this.store.buildings;
    },
    adminEntrances() {
      return this.store.entrances;
    },
    adminApartments() {
      return this.store.apartments;
    },
  }
};
</script>

<template>

  <h1>Welcome to dashboard!</h1>

  <!-- Admin role div -->
  <div v-if="this.store.userRole === 'admin'">
    <h2>Admin Section</h2>
    <p>Hello, Admin! You have full access.</p>

    <h5>Buildings (building id - building address - building number):</h5>
    <ul>
      <li v-for="building in adminBuildings" :key="building.id">
        {{ building.id }} - {{ building.address }} - {{ building.number }}
      </li>
    </ul>
    <h5>Entrances (entrance id - building id - entrance number):</h5>
    <ul>
      <li v-for="entrance in adminEntrances" :key="entrance.id">
        {{ entrance.id }} - {{ entrance.building }} - {{ entrance.number }}
      </li>
    </ul>
    <h5>Apartments (apartment id - entrance id - apartment number):</h5>
    <ul>
      <li v-for="apartment in adminApartments" :key="apartment.id">
        {{ apartment.id }} - {{ apartment.entrance }} - {{ apartment.number }}
      </li>
    </ul>
  </div>

  <!-- Manager role div -->
  <div v-else-if="this.store.userRole === 'manager'">
    <h2>Manager Section</h2>
    <p>Hello, Manager! You have access to manage entrances, apartments, guards and inhabitants.</p>
    <h5>Buildings (building id - building address - building number):</h5>
    <ul>
      <li v-for="building in this.store.manager_buildings" :key="building.id">
        {{ building.id }} - {{ building.address }} - {{ building.number }}
      </li>
    </ul>
  </div>

  <!-- Guard role div -->
  <div v-else-if="this.store.userRole === 'guard'">
    <h2>Guard Section</h2>
    <p>Hello, Guard! You have access to manage apartments and inhabitants.</p>

    <h5>Entrances (entran•••••ce id - building id - entrance number):</h5>
    <ul>
      <li v-for="entrance in this.store.guard_entrances" :key="entrance.id">
        {{ entrance.id }} - {{ entrance.building }} - {{ entrance.number }}
      </li>
    </ul>
  </div>

  <!-- Inhabitant role div -->
  <div v-else-if="this.store.userRole === 'inhabitant'">
    <h2>Inhabitant Section</h2>
    <p>Hello, Inhabitant! You have access to manage nothing.</p>

    <h5>Apartments (apartment id - entrance id - apartment number):</h5>
    <ul>
      <li v-for="apartment in this.store.inhabitant_apartments" :key="apartment.id">
        {{ apartment.id }} - {{ apartment.entrance }} - {{ apartment.number }}
      </li>
    </ul>
  </div>

</template>
