# Deploy Hermes Agent to Railway.app

Railway.app makes it super easy to deploy Docker applications online. Here's how:

## Prerequisites

1. **GitHub Account** - You already have this ✅
2. **Railway Account** - Create one at https://railway.app (free tier available)

---

## Step 1: Create a Railway Account

1. Go to https://railway.app
2. Click **"Start Project"**
3. Sign up with **GitHub** (easiest method)
4. Authorize Railway to access your GitHub

---

## Step 2: Connect Your Repository

1. In Railway dashboard, click **"+ New Project"**
2. Select **"Deploy from GitHub repo"**
3. Search for and select: `arafat33-1525-star/hermes`
4. Click **"Deploy"**

Railway will automatically:
- Detect your `Dockerfile`
- Build the Docker image
- Deploy it online
- Give you a public URL

---

## Step 3: Configure Environment Variables

1. In Railway dashboard, go to your project
2. Click the **"hermes"** service
3. Go to the **"Variables"** tab
4. Add your environment variables from `.env.example`:
   - `AGENT_NAME=hermes`
   - `LOG_LEVEL=INFO`
   - `API_PORT=8000`
   - Any API keys or model configurations

5. Click **"Deploy"** to apply changes

---

## Step 4: Get Your Public URL

1. Go to **"Settings"** tab
2. Look for **"Domains"** or **"Generate Domain"**
3. Railway will give you a URL like: `https://hermes-production-xxxxx.railway.app`

Your Hermes agent is now **live online!** 🎉

---

## Monitoring & Logs

1. Click your **"hermes"** service
2. Go to **"Logs"** tab
3. See real-time logs of your application

---

## Update Your Application

To deploy new code:

1. Push changes to GitHub:
```bash
git add .
git commit -m "Update hermes agent"
git push origin main
```

2. Railway automatically rebuilds and redeploys! ✅

---

## Railway Free Tier

- ✅ Free $5/month credit
- ✅ Deploy multiple services
- ✅ Free SSL certificate
- ✅ GitHub integration
- ✅ Automatic deployments on git push

**After free credits:** Pay-as-you-go pricing (usually $5-20/month for small apps)

---

## Pricing Calculator

Check estimated cost: https://railway.app/pricing

---

## Troubleshooting

### Deployment Failed

1. Check **"Logs"** tab for errors
2. Common issues:
   - Missing `Dockerfile`
   - Missing `requirements.txt`
   - Port not set to `8000`
   - Environment variables not configured

### Port Issues

Railway automatically assigns a port. Make sure your app listens on:
```python
# For FastAPI/Uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
```

The port is usually provided via `$PORT` environment variable. Update your Dockerfile:

```dockerfile
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Complete Railway Deployment Flow

```
1. Sign up at railway.app (with GitHub)
   ↓
2. Create new project
   ↓
3. Connect your GitHub repo
   ↓
4. Add environment variables
   ↓
5. Deploy automatically starts
   ↓
6. Get public URL
   ↓
7. Your Hermes agent is LIVE! 🚀
```

---

## Example: Your Live Hermes Agent

Once deployed, you can:

- Access it: `https://your-url.railway.app`
- Share the URL with others
- Get real-time logs
- Scale up if needed
- Add custom domain (paid)

---

## Need Help?

- **Railway Docs:** https://docs.railway.app/
- **Docker on Railway:** https://docs.railway.app/deploy/dockerfiles
- **Railway Discord:** Join their community for support

---

**Ready to go live? Start here:** https://railway.app 🚀
