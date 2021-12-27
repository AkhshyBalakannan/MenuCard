<template>
  <div class="container">
    <div class="card mt-3 mb-2">
      <div class="card-body">
        Hello Admin, You can add the relations for Food and Meal using the
        Public ID provided below.
      </div>
    </div>
    <form method="POST" @submit.prevent="make_link">
       
      <div class="card mb-3">
        <div class="card-body">
          <div class="input-group">
            <label class="input-group-text" for="meal">Meal Public ID</label>
            <validation-provider rules="required" v-slot="{ errors }">
            <select
              id="meal"
              class="form-control"
              v-model="link.meal_public_id"
              :class="{ required_field_false: error.meal }"
              style="width:350px;"
              required
            >
              <option
                v-for="data in link_data.meal_data"
                :key="data.id"
                :value="data.public_id"
              >
                {{ data.meal_name }}
              </option>
            </select>
            <span class="required_field_false">{{ errors[0] }}</span>
            </validation-provider>
            <label class="input-group-text" for="food">Food Public ID</label>
            <validation-provider rules="required" v-slot="{ errors }">
            <select
              id="food"
              class="form-control"
              v-model="link.food_public_id"
              :class="{ required_field_false: error.food }"
              style="width:350px;"
              required
            >
              <option
                v-for="data in link_data.food_data"
                :key="data.id"
                :value="data.public_id"
              >
                {{ data.food_name }}
              </option>
            </select>
            <span class="required_field_false">{{ errors[0] }}</span>
            </validation-provider>
            <div class="input-group-postpend">
              <button class="btn btn-success" type="submit">Make Link</button>
            </div>
          </div>
        </div>
      </div>
    </form>
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
      error: {
        meal: false,
        food: false,
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
    make_link(e) {
      e.preventDefault();
      if (!(this.link.meal_public_id == "" || this.link.food_public_id == "")) {
        this.error.meal = this.error.food = false;
        this.$http
          .patch(this.$store.getters.url + "/link", this.link)
          .then((data) => {
            console.log(data);
            this.$router.go();
          });
      }
    },
  },
};
</script>

<style>
.required_field_false {
  border-color: rgb(245, 61, 61);
}
</style>
