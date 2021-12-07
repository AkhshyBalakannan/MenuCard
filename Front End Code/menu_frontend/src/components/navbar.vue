<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarTogglerDemo03"
          aria-controls="navbarTogglerDemo03"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <a class="navbar-brand" href="#">ABC-MenuCard</a>
        <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="#">Home</a>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <a class="nav-link" href="#">Check Your Menu</a>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <a class="nav-link" href="#">Foods</a>
            </li>
            &nbsp;&nbsp;
            <li class="nav-item">
              <a class="nav-link" href="#">Profile</a>
            </li>
          </ul>
          <span class="d-flex">
            <button class="btn btn-outline-warning" type="button">
              Sign In
            </button>
          </span>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: "Welcome to Your Vue.js App",
    };
  },
};
</script>

<style>
</style>
