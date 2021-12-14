<template>
  <div>
    LINK COMPONENT
    {{ link_data }}
    <input
      type="text"
      v-model="link.meal_public_id"
      placeholder="meal public ID"
    />
    <input
      type="text"
      v-model="link.food_public_id"
      placeholder="food public ID"
    />
    <button @click.prevent="make_link">Make Link</button>
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
    this.$http
      .get(this.$store.getters.url + "/link?t=" + this.$cookie.get("token"))
      .then((data) => {
        console.log(data);
        this.link_data = data.body;
      });
  },
  methods: {
    make_link() {
      this.$http
        .patch(
          "http://localhost:5000/link?t=" + this.$cookie.get("token"),
          this.link
        )
        .then((data) => {
          console.log(data);
        });
    },
  },
};
</script>

<style>
</style>
