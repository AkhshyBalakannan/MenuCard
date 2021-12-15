<template>
  <div>
    <body>
      <div id="main">
        <div id="photo">
          <img
            src="https://images.unsplash.com/photo-1544502062-f82887f03d1c?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1427&q=80"
            id="profilepic"
          />
        </div>
        <div id="info">
          <div id="name">
            <h2>{{ user_data.username }}</h2>
            <h3>{{ user_data.email }}</h3>
          </div>
          <div id="contacts">
            <div class="link" id="github">
              <h4>{{ user_data.public_id }}</h4>
            </div>
            <div class="link" id="insta">
              <h4>{{ user_data.admin }}</h4>
            </div>
            <div class="link" id="dribbble">
              <a
                href="https://dribbble.com/beetran"
                style="color: rgba(255, 255, 255, 0.6)"
                ><i class="fab fa-dribbble"></i
              ></a>
            </div>
          </div>
        </div>
      </div>
    </body>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user_data: [],
    };
  },
  created() {
    if (this.$cookie.get("token")) {
      this.$http
        .get(
          this.$store.getters.url +
            "/user/profile?t=" +
            this.$cookie.get("token")
        )
        .then(function (data) {
          this.user_data = data.body;
        });
    } else {
      this.$router.push("/signin?next=" + this.$router.history.current.path);
    }
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap");

body {
  font-family: "Montserrat", sans-serif;
  background: #673ab7; /* fallback for old browsers */
  background: linear-gradient(
    to right,
    #111536,
    #161a3f
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background-image: url("https://cdn.osxdaily.com/wp-content/uploads/2020/10/macos-big-sur-wallpaper-2-scaled.jpg");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}

#main {
  display: grid;

  grid-template-columns: 40% 60%;
  max-width: 500px;
  height: 450.5px;
  background: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0.4)
  );
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 10px;
  border: 1px solid rgba(255, 255, 255, 0.18);

  margin: auto;
  margin-top: 140px;
}
#name {
  color: rgba(255, 255, 255, 0.6);
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding: 0 40px;
}
#profilepic {
  height: 140px;
  width: 140px;
  box-shadow: 0 0 42px 0 rgba(255, 255, 255, 0.17);
  background: rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 10px;
  border: 3px solid rgba(255, 255, 255, 0.18);
  border-radius: 50%;
  object-fit: cover;
  object-position: 50% 10%;
}
#photo {
  display: flex;
  justify-content: center;
  align-items: center;
}

#info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.link {
  background: rgba(255, 255, 255, 0.25);
  box-shadow: 0 0px 32px 0 rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  display: block;
  font-size: 40px;
  padding: 4px;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  margin: 10px;
  cursor: pointer;
}

.link:hover {
  transform: translateY(-2px);
  transition: all 0.5s;
  background: rgba(255, 255, 255, 0.5);
}

#github:hover a {
  background: -webkit-linear-gradient(rgb(124, 0, 124), #333);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#insta:hover a {
  background: -webkit-linear-gradient(45deg, #f6ce6d, #dd2b68, #ae32a9);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#dribbble:hover a {
  background: -webkit-linear-gradient(45deg, #e45189, #e04b85);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#contacts {
  display: flex;
  flex-direction: row;
}
</style>
