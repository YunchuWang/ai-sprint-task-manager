<template>
  <div id="app">
    <ResponsePanel :messages="messages" />
    <InputPanel @task-sent="handleTaskSent" />
  </div>
</template>

<script>
import InputPanel from './components/InputPanel.vue';
import ResponsePanel from './components/ResponsePanel.vue';

export default {
  name: 'App',
  components: {
    InputPanel,
    ResponsePanel
  },
  data() {
    return {
      messages: []
    };
  },
  methods: {
    handleTaskSent(task) {
      this.addMessage('User', task);
      this.generateResponse(task);
    },
    addMessage(sender, text) {
      this.messages.push({
        id: this.messages.length + 1,
        sender,
        text
      });
    },
    generateResponse(task) {
      // Simulate an AI response
      const response = `Task "${task}" added successfully!`;
      this.addMessage('AI', response);
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f9;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}

#chat-container {
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 80%;
  max-width: 600px;
  display: flex;
  flex-direction: column;
}
</style>
