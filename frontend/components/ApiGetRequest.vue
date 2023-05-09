<script setup>
import axios from "axios";
import { onMounted, reactive } from "vue";

let data = reactive({
  title: 'Hello World',
  contentList: []
})
// let title = ref("Hello World");
// let contentList = ref([]);

onMounted(async () => {
  let response;
  try {
    response = await axios.get("/api/posts/")
  } catch (error) {
    response = error.response;
    data.title = "Api Error";
  }
  if (response.status === 200) {
    let responseData = response.data
    data.title = "Post";
    data.contentList = responseData.data;
  } else {
    return "Api error";
  }
});
</script>

<template>
  <div>
    <h1>{{ data.title }}</h1>
    <div v-for="post of data.contentList" :key="post.id">
      <h2>{{ post.id }} - {{ post.title }}</h2>
    </div>
  </div>
</template>
