<template>
  <div>
    <div class="card mt-3 mb-2">
      <div class="card-body">
        <p>Hello Admin, You can <b>Promote, Delete</b> User Accounts below.</p>
        <p>
          If you Need to delete your account you need to change to profile route
          and click on Delete Profile
        </p>
      </div>
    </div>
    <div class="card mt-3 mb-2">
      <div class="card-body">
        <div class="row mt-3 px-5">
          <div class="col">
            <h5>User List</h5>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">User Name</th>
                  <th scope="col">Mail ID</th>
                  <th scope="col">Admin</th>
                  <th scope="col-1">Promote</th>
                  <th scope="col-1">Delete</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="data in user_data"
                  v-if="same_username(data.username)"
                  :key="data.id"
                >
                  <td class="col">
                    {{ data.username }}
                  </td>
                  <td class="col">{{ data.email }}</td>
                  <td class="col">{{ data.admin }}</td>
                  <td class="col-2">
                    <div class="row">
                      &nbsp;<span
                        class="btn btn-primary col"
                        @click.prevent="promote_user(data.public_id)"
                        >Promote</span
                      >
                    </div>
                  </td>
                  <td class="col-2">
                    <div class="row">
                      <span
                        class="btn btn-danger col"
                        @click.prevent="delete_user(data.public_id)"
                        >Delete</span
                      >
                    </div>
                  </td>
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
      user_data: [],
      logged_user: "",
      message: "",
    };
  },
  created() {
    this.$http
      .get(this.$store.getters.url + "/user/profile")
      .then(function (data) {
        this.logged_user = data.body.username;
      });
    this.$http.get(this.$store.getters.url + "/user/all").then(function (data) {
      this.user_data = data.data;
    });
  },
  methods: {
    delete_user(data) {
      this.$http
        .delete(this.$store.getters.url + "/user/delete/" + data)
        .then((data) => {
          this.$router.go();
        });
    },
    promote_user(data) {
      this.$http
        .put(this.$store.getters.url + "/user/promote/" + data)
        .then((data) => {
          this.$router.go();
        });
    },
  },
  computed: {
    // a computed getter
    same_username: function () {
      // `this` points to the vm instance
      return function (username) {
        if (this.logged_user == username) return false;
        return true;
      };
    },
  },
};
</script>

<style>
</style>
