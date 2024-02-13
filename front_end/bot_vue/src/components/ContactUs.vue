<template>
  <div class="contact-us">
    <h2>Contact Us</h2>
    
    <p>
      If you have concerns or wish to report any issues, please visit our whistleblowing website:
      <a :href="whistleblowingWebsite" target="_blank" rel="noopener noreferrer" aria-label="Open Whistleblowing Website in a new tab">Whistleblowing Website</a>
    </p>

    <div class="contact-details">
      <h3>Contact Details</h3>
      <p>Email: {{ contactEmail }}</p>
      <p>Phone: {{ contactPhone }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      whistleblowingWebsite: 'https://www.example-whistleblowing.com',
      contactEmail: 'ethics@example.com',
      contactPhone: '+1234567890',
    };
  },
};
</script>

<style scoped>
.contact-us {
  position: fixed;
  bottom: 30px;
  left: 49%;
  transform: translateX(-50%);
  background-color: #f0f0f0;
  padding: 10px;
  text-align: center;
  max-width: 500px;
  max-height: 180px;
  margin: 0 auto; /* Center the box horizontally */
  z-index: 1;
}

.contact-details {
  margin-top: 10px;
}

.contact-details h3 {
  font-size: 1em;
}

.contact-details p {
  margin: 5px 0;
  font-size: 1em;
}

@media (max-width: 768px) {
  .contact-us {
    position: static;
    max-width: 100%;
  }
}
</style>
