<script>
import { RouterView } from "vue-router";
import { useStore } from "../stores/store.js";

export default {
  data() {
    return {
      store: useStore(),
    };
  },

  async mounted() {},
};
</script>
<template>
  <RouterView />
</template>
