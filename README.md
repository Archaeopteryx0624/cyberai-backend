# CyberAI - AI-Powered Cybersecurity Website

A modern, hacker-themed website for showcasing AI-powered cybersecurity solutions featuring DeepSeek Coder.

## Features

- **Modern Hacker Aesthetic**: Matrix rain effect, terminal-style design, glowing green theme
- **Contact Form**: Messages stored in localStorage and viewable in admin dashboard
- **Admin Dashboard**: View, respond to, and manage incoming messages
- **Responsive Design**: Works on all devices
- **Blog Section**: Showcase security insights and articles

## Pages

1. **index.html** - Main landing page with features and contact form
2. **blog.html** - Blog posts about AI and cybersecurity
3. **admin.html** - Admin dashboard for managing messages

## Setup Instructions

### Option 1: EmailJS Integration (Recommended for Production)

1. Sign up at [emailjs.com](https://www.emailjs.com/)
2. Create an email service (Gmail recommended)
3. Create an email template with these variables:
   - `{{name}}`
   - `{{email}}`
   - `{{subject}}`
   - `{{message}}`
4. In `index.html`, uncomment the EmailJS SDK line:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js"></script>
   ```
5. Replace the form submission code with:
   ```javascript
   emailjs.init('YOUR_PUBLIC_KEY');
   emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', formData)
       .then(() => {
           // Success handling
       }, (error) => {
           // Error handling
       });
   ```

### Option 2: Netlify Forms (Easiest)

1. Add `data-netlify="true"` to the form tag in index.html:
   ```html
   <form id="contactForm" data-netlify="true">
   ```
2. Netlify will automatically handle form submissions
3. View submissions in your Netlify dashboard

### Option 3: Current Setup (LocalStorage)

- Messages are stored in browser localStorage
- Viewable in admin.html
- Responses open Gmail compose window
- Good for testing/demo purposes

## Deployment to Netlify

### Method 1: Drag and Drop

1. Go to [netlify.com](https://www.netlify.com/)
2. Sign up/login
3. Drag the entire folder to Netlify's deploy zone
4. Your site is live!

### Method 2: Git Deployment

1. Create a Git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
2. Push to GitHub/GitLab
3. Connect repository to Netlify
4. Netlify will auto-deploy on every push

## About DeepSeek Coder Deployment

### Important: DeepSeek Coder Cannot Run on Netlify

Netlify is a **static site host** and cannot run:
- GGUF models
- Ollama
- Any AI inference
- Backend processes
- GPU/CPU intensive tasks

### Alternative Deployment Options for DeepSeek Coder:

#### Option 1: Separate Backend Server
- Deploy the website on Netlify (frontend only)
- Run DeepSeek Coder on:
  - **AWS EC2** with GPU instance
  - **DigitalOcean Droplet** 
  - **Your own VPS** with Ollama installed
  - **Railway.app** or **Render.com** (for smaller models)
- Connect frontend to backend via API

#### Option 2: Cloud AI Services
- Use **Replicate.com** to host your model
- Use **Hugging Face Inference API**
- Call the API from your static site

#### Option 3: Serverless with Modal/RunPod
- Deploy model on **Modal.com** or **RunPod.io**
- Get API endpoint
- Call from static frontend

### Recommended Architecture:

```
┌─────────────────┐
│   Netlify       │
│  (Static Site)  │
│  index.html     │
│  blog.html      │
│  admin.html     │
└────────┬────────┘
         │
         │ API Calls
         │
         ▼
┌─────────────────┐
│  Your Server    │
│  (VPS/Cloud)    │
│  Ollama +       │
│  DeepSeek Coder │
└─────────────────┘
```

### Setting Up DeepSeek Coder on Your Own Server:

1. **Get a Server** (Ubuntu 22.04 recommended)
   ```bash
   # Minimum specs:
   # - 8GB RAM (16GB+ recommended)
   # - 50GB storage
   # - 4 vCPUs
   ```

2. **Install Ollama**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

3. **Pull DeepSeek Coder**
   ```bash
   ollama pull deepseek-coder:6.7b
   # or for larger model:
   ollama pull deepseek-coder:33b
   ```

4. **Run Ollama API**
   ```bash
   ollama serve
   ```

5. **Expose API** (use nginx reverse proxy for production)

6. **Call from Frontend**
   ```javascript
   fetch('https://your-server.com/api/generate', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({
           model: 'deepseek-coder',
           prompt: 'Analyze this code for vulnerabilities...'
       })
   })
   ```

## File Structure

```
cybersec-site/
├── index.html          # Main page with contact form
├── blog.html          # Blog/articles page
├── admin.html         # Admin dashboard
└── README.md          # This file
```

## Customization

- **Colors**: Edit CSS variables in `:root` section
- **Content**: Update text directly in HTML files
- **Email**: Configure EmailJS or Netlify Forms
- **Blog Posts**: Add more blog cards in blog.html

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Notes

- Admin dashboard uses localStorage - data persists per browser
- For production, consider backend database for messages
- Gmail responses require Gmail account signed in
- Matrix effect may affect performance on low-end devices

## License

MIT License - Free to use and modify

## Support

For issues or questions about the website, check the code comments or contact support.

For DeepSeek Coder model questions, visit: https://github.com/deepseek-ai/DeepSeek-Coder
