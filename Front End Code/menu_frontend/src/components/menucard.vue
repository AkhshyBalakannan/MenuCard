<template>
  <div>
    <div class="app-body">
      {{meal_data}}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_token : "",
      meal_data : []
    };
  },
  created(){
    if (this.$cookie.get("token")){
      this.user_token = this.$cookie.get("token")
      this.$http.get('http://localhost:5000/meal/all?t='+this.user_token)
      .then(function(data){
          // console.log(data)
          this.meal_data = data.body
        }
      );
    }
    else{
      this.$router.push('/signin?next='+this.$router.history.current.path);
    }
  }
};
</script>

<style scoped>
.app-body {
  background-color: azure;
}
</style>
