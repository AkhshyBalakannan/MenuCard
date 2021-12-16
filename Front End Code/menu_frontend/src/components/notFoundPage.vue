<template>
  <div class="container mt-5 px-5">
    <h1>Sorry! the URL <span>{{ url }}</span> your trying to reach doesn't exists</h1>
    <router-link to="/menucard">Go Back to MenuCard</router-link>
  </div>
</template>

<script>
export default {
  data() {
    return {
        url:this.$route.fullPath,
    };
  }
};
</script>

<style scoped>
span{
    color: red;
}
</style>