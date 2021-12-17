<template>
  <div>
    <div class="card mt-3 mb-2">
      <div class="card-body">
        <p>Hello Admin, You can <b>Add, Edit, Delete</b> Meal details below.</p>
      </div>
    </div>
    <div class="card mb-3">
      <div class="card-body px-5">
        <h5>Add New Meal</h5>
        <div class="input-group">
          <input
            type="text"
            class="form-control"
            v-model="add_meal_data.meal_name"
            placeholder="Meal Name"
          />
          <div class="input-group-postpend">
            <button class="btn btn-success" @click.prevent="add_meal">
              Add Meal
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="row mt-3 px-5">
      <div class="col">
        <h5>Meal List</h5>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Meal Name</th>
              <th scope="col">Public ID</th>
              <th scope="col-1">Update Meal</th>
              <th scope="col-1">Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in meals_data" :key="data.id">
              <td class="col">{{ data.meal_name }}</td>
              <td class="col">{{ data.public_id }}</td>
              <td class="col-2">
                <div class="row">
                  <input
                    type="text"
                    v-model.lazy="update.meal_name"
                    class="form-control col"
                  />&nbsp;<span
                    class="btn btn-primary col"
                    @click.prevent="update_meal(data.public_id)"
                    >Update</span
                  >
                </div>
              </td>
              <td class="col-1">
                <span
                  class="btn btn-danger"
                  @click.prevent="delete_meal(data.public_id)"
                  >Delete</span
                >
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      add_meal_data: {
        meal_name: "",
      },
      meals_data: [],
      delete_public_id: "",
      update: {
        meal_name: "",
        public_id: "",
      },
    };
  },
  methods: {
    add_meal() {
      this.$http
        .post(this.$store.getters.url + "/meal/create", this.add_meal_data)
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
    delete_meal(data) {
      this.delete_public_id = data;
      console.log("Entering Meal Delete Function");
      this.$http
        .delete(
          this.$store.getters.url + "/meal/delete/" + this.delete_public_id
        )
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
    update_meal(data) {
      this.update.public_id = data;
      console.log("Entering Food Update Function");
      this.$http
        .patch(this.$store.getters.url + "/meal/update", this.update)
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
  },
  beforeMount() {
    this.$http.get(this.$store.getters.url + "/meal/types").then((data) => {
      console.log(data);
      this.meals_data = data.body;
    });
  },
};
</script>

<style>
</style>
