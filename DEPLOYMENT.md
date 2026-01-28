# 🚀 Complete Deployment Guide - Render.com + Netlify

## Overview

Your site has 2 parts:
1. **Frontend** (HTML/CSS/JS) → Deploy to **Netlify** (FREE)
2. **Backend** (DeepSeek Coder AI) → Deploy to **Render.com** (FREE)

---

## Part 1: Deploy Backend to Render.com (FREE Tier)

### Step 1: Prepare Your Backend Files

You need these files in a folder called `backend/`:
- `Dockerfile`
- `app.py`
- `requirements.txt`
- `start.sh`
- `render.yaml` (optional)

### Step 2: Create GitHub Repository

```bash
# Create a new repository
cd backend
git init
git add .
git commit -m "Initial backend commit"

# Push to GitHub (create a new repo on GitHub first)
git remote add origin https://github.com/YOUR_USERNAME/cyberai-backend.git
git push -u origin main
```

### Step 3: Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign up/Login (free account)
3. Click **"New +"** → **"Web Service"**
4. Connect your GitHub account
5. Select your `cyberai-backend` repository
6. Configure:
   - **Name**: cyberai-backend
   - **Region**: Choose closest to you
   - **Branch**: main
   - **Root Directory**: `.` (or `/backend` if backend is in subfolder)
   - **Environment**: Docker
   - **Plan**: FREE
   - **Auto-Deploy**: Yes

7. Click **"Create Web Service"**

### Step 4: Wait for Deployment

- First deploy takes **10-15 minutes** (pulling model)
- Watch the logs to see progress
- Your URL will be: `https://cyberai-backend.onrender.com`

### ⚠️ Important Notes About Render Free Tier:

- **Spins down after 15 minutes** of inactivity
- Takes **30-60 seconds** to wake up on first request
- **750 hours/month free** (runs 24/7 for entire month)
- If you hit limits, just wait until next month

---

## Part 2: Deploy Frontend to Netlify (FREE Forever)

### Step 1: Update API URL

Open `demo.html` and update line ~192:

```javascript
const API_BASE_URL = 'https://cyberai-backend.onrender.com'; // Your Render URL
```

### Step 2: Deploy to Netlify

**Method A: Drag & Drop (Easiest)**

1. Go to [netlify.com](https://www.netlify.com)
2. Sign up/Login
3. Drag these files to deploy zone:
   - `index.html`
   - `blog.html`
   - `admin.html`
   - `demo.html`
4. Done! Your site is live!

**Method B: Git Deployment**

1. Create GitHub repo with frontend files
2. Connect to Netlify
3. Auto-deploys on every push

### Step 3: Optional - Custom Domain

1. In Netlify dashboard → **Domain Settings**
2. Add your custom domain
3. Follow DNS instructions

---

## 🧪 Testing Your Deployment

### Test Backend

```bash
# Check health
curl https://cyberai-backend.onrender.com/health

# Test code analysis
curl -X POST https://cyberai-backend.onrender.com/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "function test() { eval(userInput); }"}'
```

### Test Frontend

1. Go to your Netlify URL
2. Click **"AI DEMO"** in navigation
3. Check backend status (should show online/offline)
4. Try analyzing some code

---

## 📊 Monitoring & Logs

### Render Logs

1. Go to Render dashboard
2. Click your service
3. View **Logs** tab
4. See real-time output

### Netlify Analytics

1. Go to Netlify dashboard
2. View traffic and performance
3. Check form submissions (if using Netlify Forms)

---

## ⚙️ Configuration

### Environment Variables (If Needed)

In Render dashboard:
1. Go to your service
2. Click **Environment** tab
3. Add variables:
   - `PORT=5000` (already set)
   - Add any API keys here

### CORS Issues?

The Flask backend has CORS enabled for all origins. If you still have issues:

```python
# In app.py, specify your Netlify domain:
CORS(app, resources={r"/api/*": {"origins": "https://your-site.netlify.app"}})
```

---

## 🐛 Troubleshooting

### Backend Issues

**Problem: Service won't start**
- Check Render logs for errors
- Make sure Dockerfile syntax is correct
- Verify all files are committed to git

**Problem: Model fails to load**
- DeepSeek 1.3B needs ~2GB RAM
- Free tier has 512MB (may be tight)
- Try smaller model: `ollama pull deepseek-coder:base` (if available)

**Problem: Timeout errors**
- First request takes 30-60s (waking up)
- Model inference can take 20-30s
- This is normal on free tier

### Frontend Issues

**Problem: Can't connect to backend**
- Make sure API_BASE_URL is correct
- Check backend is online (visit /health endpoint)
- Check browser console for CORS errors

**Problem: Demo not working**
- Open browser DevTools (F12)
- Check Console for errors
- Verify backend URL is set

---

## 💰 Cost Breakdown

### Current Setup (100% FREE):

- **Netlify**: $0/month (100GB bandwidth)
- **Render**: $0/month (750 hours)
- **Total**: $0/month

### If You Outgrow Free Tier:

- **Render Starter**: $7/month (keeps service always on)
- **Netlify Pro**: $19/month (more bandwidth)
- **Better Server**: $10-20/month (DigitalOcean, etc.)

---

## 🔄 Updating Your Site

### Update Frontend

1. Edit HTML files
2. Re-deploy to Netlify (drag & drop or git push)

### Update Backend

1. Edit backend files
2. Commit and push to GitHub
3. Render auto-deploys

---

## 📈 Scaling Tips

### When You Need More Power:

1. **Upgrade Render plan** ($7/month for always-on)
2. **Use larger model** (6.7B or 33B version)
3. **Add Redis cache** for faster responses
4. **Move to dedicated server** with GPU

### Production Improvements:

1. **Add authentication** to admin panel
2. **Database** instead of localStorage
3. **Rate limiting** on API endpoints
4. **CDN** for static assets
5. **Monitoring** with Sentry or LogRocket

---

## 🎯 Next Steps

1. ✅ Deploy backend to Render
2. ✅ Get backend URL
3. ✅ Update demo.html with URL
4. ✅ Deploy frontend to Netlify
5. ✅ Test everything works
6. 🎉 Share your site!

---

## 📚 Useful Links

- [Render Documentation](https://render.com/docs)
- [Netlify Documentation](https://docs.netlify.com)
- [Ollama Documentation](https://ollama.ai/docs)
- [DeepSeek Coder GitHub](https://github.com/deepseek-ai/DeepSeek-Coder)

---

## 🆘 Need Help?

- **Render Issues**: Check their [Discord](https://discord.gg/render)
- **Netlify Issues**: Check their [Forums](https://answers.netlify.com)
- **Ollama Issues**: Check their [GitHub Issues](https://github.com/ollama/ollama/issues)

---

## ✨ Bonus: EmailJS Integration

Want real email notifications instead of localStorage?

1. Sign up at [emailjs.com](https://www.emailjs.com)
2. Create email template
3. Add to `index.html`:

```javascript
emailjs.init('YOUR_PUBLIC_KEY');
emailjs.send('SERVICE_ID', 'TEMPLATE_ID', {
    name: formData.name,
    email: formData.email,
    message: formData.message
});
```

---

Good luck with your deployment! 🚀
 
