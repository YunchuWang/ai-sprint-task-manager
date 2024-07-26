<template>
  <div id="response-panel">
    <div v-for="message in messages" :key="message.id">
      <strong>{{ message.sender }}:</strong> {{ message.text }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    messages: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
#response-panel {
  width: 340px;
  height: 300px;
  overflow-y: auto;
  background-color:azure;
  border-bottom: 1px solid #dddddd;
}


#response-panel div {
  margin-bottom: 10px;
  word-wrap: break-word;
}

div {
  margin-bottom: 10px;
}
</style>
