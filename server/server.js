// server.js
const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 5000;

// API endpoint to trigger summarization
app.post('/summarize', async (req, res) => {
  const { url, style, depth } = req.body;
  
  try {
    // Step 1: Fetch blog content
    const content = await fetchBlogContent(url); 
    
    // Step 2: Send to Python AI service
    const summary = await axios.post('http://localhost:5001/process', {
      content,
      style,
      depth
    });

    res.json(summary.data);
  } catch (error) {
    res.status(500).json({ error: 'Summarization failed' });
  }
});

// Public API integration example
async function fetchBlogContent(url) {
  // Use Mercury Parser or similar
  const response = await axios.get(`https://mercury.postlight.com/parser?url=${url}`, {
    headers: {'x-api-key': process.env.MERCURY_API_KEY}
  });
  return response.data.content;
}

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));