<template>
  <div class="container">
    <div class="card mt-3 mb-2">
      <div class="card-body">
        Hello Admin, You can add the relations for Food and Meal using the
        Public ID provided below.
      </div>
    </div>
    <div class="card mb-3">
      <div class="card-body">
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            v-model="link.meal_public_id"
            placeholder="MEAL PUBLIC ID"
          />
          <input
            type="text"
            class="form-control"
            v-model="link.food_public_id"
            placeholder="FOOD PUBLIC ID"
          />
          <div class="input-group-postpend">
            <button class="btn btn-success" @click.prevent="make_link">
              Make Link
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-body">
        <div class="row">
          <div class="col">
            <h3>Food List</h3>
            <table class="table">
              <thead>
                <tr>
                  <!-- <th scope="col">#</th> -->
                  <th scope="col">Food Name</th>
                  <th scope="col">Public ID</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="data in link_data.food_data" :key="data.id">
                  <!-- <th scope="row">{{ data.id }}</th> -->
                  <td>{{ data.food_name }}</td>
                  <td>{{ data.public_id }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="col">
            <h3>Meal List</h3>
            <table class="table">
              <thead>
                <tr>
                  <!-- <th scope="col">#</th> -->
                  <th scope="col">Meal Name</th>
                  <th scope="col">Public ID</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="data in link_data.meal_data" :key="data.id">
                  <!-- <th scope="row">{{ data.id }}</th> -->
                  <td>{{ data.meal_name }}</td>
                  <td>{{ data.public_id }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      link_data: [],
      link: {
        meal_public_id: "",
        food_public_id: "",
      },
    };
  },
  beforeMount() {
    this.$http.get(this.$store.getters.url + "/link").then((data) => {
      console.log(data);
      this.link_data = data.body;
    });
  },
  methods: {
    make_link() {
      this.$http
        .patch(this.$store.getters.url + "/link", this.link)
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
  },
};
</script>

<style>
</style>
