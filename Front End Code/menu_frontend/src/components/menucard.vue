<template>
  <div class="container app-body">
    <app-navbar></app-navbar>
    {{ msg }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
    };
  },
};
</script>

<style scoped>
.app-body {
  background-color: azure;
}
</style>
