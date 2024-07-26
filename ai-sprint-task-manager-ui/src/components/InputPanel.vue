<template>
    <div id="input-panel">
      <textarea v-model="task" placeholder="Enter your task..." @keyup.enter="sendTask"></textarea>
      <button @click="sendTask">Send</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        task: ''
      };
    },
    methods: {
      sendTask() {
        if (this.task) {
          this.$emit('task-sent', this.task);
          this.task = '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  #input-panel {
    display: flex;
    padding: 10px;
  }
  
  textarea {
    flex: 1;
    padding: 10px;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin-right: 10px;
    box-sizing: border-box;
    resize: vertical; /* Allow vertical resizing, disable horizontal resizing */
    height: 40px; /* Default height */
    min-height: 40px; /* Minimum height */
    max-height: 200px; /* Maximum height */
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-sizing: border-box;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  