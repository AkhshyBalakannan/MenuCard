<template>
  <div>
      MEAL COMPONENT
      <router-view></router-view>
  </div>
</template>

<script>
import store from "../store";
export default {
  data() {
    return {
      food_data : []
    };
  }
};
</script>

<style scoped>
.app-body {
  background-color: azure;
}
</style>
