<template>
  <div class="container">
    <div class="card mt-3 mb-2">
      <div class="card-body">
        Hello Admin, You can add the relations for Food and Meal using the
        Public ID provided below. You can also Delete the links made before by
        clicking the food button below in Relation List Table with respective
        Meal Name
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
                style="width: 350px"
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
                style="width: 350px"
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
    <div class="card mb-3">
      <div class="card-body">
        <h3>Relation List</h3>
        <table style="width: 90%; margin-left: 5%">
          <thead>
            <tr class="row">
              <th class="col-3">Meal Name</th>
              <th class="col">Related Foods</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in menu_data" :key="data.id" class="row">
              <hr />
              <td class="col-3">{{ data.meal_name }}</td>
              <td class="col">
                <span
                  v-for="(food_data, key) of data.meal_food"
                  :key="key"
                  style="justify-content: center"
                >
                  <button
                    class="btn btn-danger"
                    @click="set_value(food_data.public_id, data.public_id)"
                  >
                    {{ food_data.food_name }}</button
                  >&nbsp;
                </span>
              </td>
            </tr>
          </tbody>
        </table>
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
      menu_data: [],
      link: {
        meal_public_id: "",
        food_public_id: "",
      },
      unlink: {
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
    this.$http.get(this.$store.getters.url + "/meal/all").then((data) => {
      console.log(data);
      this.menu_data = data.body;
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
    set_value(food_public_id, meal_public_id) {
      this.unlink.food_public_id = food_public_id;
      this.unlink.meal_public_id = meal_public_id;
      this.undo_link();
    },
    undo_link() {
      this.$http
        .patch(this.$store.getters.url + "/unlink", this.unlink)
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
  },
};
</script>

<style>
.required_field_false {
  border-color: rgb(245, 61, 61);
}
</style>
