<template>
  <div>
    <router-view></router-view>
    <div class="row mt-3">
      <div class="col"></div>
      <div class="col-6">
        <h3>Food List</h3>
        <table class="table table-dark table-striped">
          <thead>
            <tr>
              <th scope="col">Food Name</th>
              <th scope="col">Public ID</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in food_data" :key="data.id">
              <td class="col">{{ data.food_name }}</td>
              <td class="col">{{ data.public_id }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col"></div>
    </div>
  </div>
</template>

<script>
import store from "../store";
export default {
  data() {
    return {
      food_data: [],
    };
  },
  beforeMount() {
    this.$http
      .get(this.$store.getters.url + "/food/all?t=" + this.$cookie.get("token"))
      .then((data) => {
        console.log(data);
        this.food_data = data.body;
      });
  },
};
</script>

<style>
</style>
