<template>
  <div>
    <div class="card mt-3 mb-2">
      <div class="card-body">
        <p>Hello Admin, You can <b>Add, Edit, Delete</b> Food details below.</p>
      </div>
    </div>
    <form method="post" @submit.prevent="add_food">
      <validation-provider rules="required" v-slot="{ errors }">
        <div class="card mb-3">
          <div class="card-body px-5">
            <h5>Add New Food</h5>
            <div class="input-group">
              <input
                type="text"
                class="form-control"
                v-model="add_food_data.food_name"
                name="add_food_data.food_name"
                placeholder="Food Name"
                required
              />

              <div class="input-group-postpend">
                <button type="submit" class="btn btn-success" >
                  Add Food
                </button>
              </div>
            </div>
            <span class="required_field_false">{{ errors[0] }}</span>
          </div>
        </div>
      </validation-provider>
    </form>
    <div class="row mt-3 px-5">
      <div class="col">
        <h5>Food List</h5>
        <table class="table">
          <thead>
            <tr>
              <th scope="col">Food Name</th>
              <th scope="col">Public ID</th>
              <th scope="col-1">Update</th>
              <th scope="col-1">Delete</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="data in foods_data" :key="data.id">
              <td class="col">
                {{ data.food_name }}
              </td>
              <td class="col">{{ data.public_id }}</td>
              <td class="col-2">
                <div class="row">
                  <input
                    type="text"
                    v-model.lazy="update.food_name"
                    class="form-control col"
                  />&nbsp;<span
                    class="btn btn-primary col"
                    @click.prevent="update_food(data.public_id)"
                    >Update</span
                  >
                </div>
              </td>
              <td class="col-1">
                <span
                  class="btn btn-danger"
                  @click.prevent="delete_food(data.public_id)"
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
      add_food_data: {
        food_name: "",
      },
      error: {
        food: false,
      },
      url: "",
      foods_data: [],
      delete_public_id: "",
      update: {
        food_name: "",
        public_id: "",
      },
    };
  },
  beforeMount() {
    this.$http.get(this.$store.getters.url + "/food/all").then((data) => {
      console.log(data);
      this.foods_data = data.body;
    });
  },
  methods: {
    add_food(e) {
      e.preventDefault();
      this.$http
        .post(this.$store.getters.url + "/food/create", this.add_food_data)
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
    delete_food(data) {
      this.delete_public_id = data;
      console.log("Entering Food Delete Function");
      this.$http
        .delete(
          this.$store.getters.url + "/food/delete/" + this.delete_public_id
        )
        .then((data) => {
          console.log(data);
          this.$router.go();
        });
    },
    update_food(data) {
      if (!(this.update.food_name == "")) {
        this.update.public_id = data;
        console.log("Entering Food Update Function");
        this.$http
          .patch(this.$store.getters.url + "/food/update", this.update)
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
  color: rgb(245, 61, 61);
}
</style>

