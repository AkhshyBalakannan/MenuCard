<template>
  <div>
    <div class="app-body">
      {{ user_data.admin }}
      {{ user_data.username }}
      {{ user_data.email }}
      {{ user_data.public_id }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data : []
    };
  },
  created(){
    if (this.$cookie.get("token")){
      this.$http.get('http://localhost:5000/user/profile?t='+this.$cookie.get("token"))
      .then(function(data){
          console.log(data)
          this.user_data = data.body
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
