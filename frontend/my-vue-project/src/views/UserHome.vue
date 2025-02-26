<template>
  <div>
    <h2>User Home</h2>
    <button @click="logout">Logout</button>
    
  </div>
</template>

<script>


export default {
  name: "UserHome",
  data() {
    return {
      users: []
    };
  },
  
  methods: {
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/login');
    }
  }
};
</script>
