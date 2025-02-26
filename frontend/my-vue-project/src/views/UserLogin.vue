<template>
  <div>
    <h2>User Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" required />
      <input type="password" v-model="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "UserLogin",
  data() {
    return {
      username: '',
      password: ''
    };
  },

  
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          username: this.username,
          password: this.password
        });


        localStorage.setItem('token', response.data.access);
        this.$router.push('/home');

      } catch (error) {
        console.error('Login failed:', error);
      }
    }
  }
};
</script>
