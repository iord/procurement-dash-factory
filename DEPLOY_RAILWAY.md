# Deploy to Railway - Complete Guide

## ✅ All Features Implemented

### Core Features:
1. ✅ **Multi-source data** (TED EU, SAM.gov, KIMDIS, Diavgeia)
2. ✅ **Authentication** with login/signup + Google OAuth ready
3. ✅ **User Personal Dashboard** with favorites
4. ✅ **Power BI Style Dashboards** with tabs and minimal scrolling
5. ✅ **Key Performance Indicators** (KPIs) on every dashboard
6. ✅ **Data Source Analysis** - Dataset types and statistics
7. ✅ **Responsive Design** - Works on all devices
8. ✅ **API Access** - Full REST API with Swagger docs

### Dashboard Features:
- ✅ Tab-based navigation (Overview, Category, Geography, Value, Timeline)
- ✅ Minimal scrolling - all charts visible
- ✅ Real-time KPIs at top
- ✅ Interactive Plotly charts
- ✅ Favorite/bookmark system

### User Features:
- ✅ Personal dashboard after login
- ✅ Save favorite tenders
- ✅ Quick stats
- ✅ Recent activity tracking
- ✅ Quick actions menu

---

## Railway Deployment Steps

### 1. Prerequisites

- Railway account (sign up at https://railway.app/)
- GitHub account
- Git installed locally

### 2. Push to GitHub

```bash
# Initialize git (if not already done)
cd procurement-dash-factory
git init
git add .
git commit -m "feat: complete procurement platform v2.0 with all features"

# Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/procurement-dash-factory.git
git branch -M main
git push -u origin main
```

### 3. Deploy on Railway

#### Option A: Via GitHub (Recommended)

1. **Login to Railway**
   - Go to https://railway.app/
   - Click "Login" and connect with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `procurement-dash-factory`

3. **Configure Environment Variables**
   - Click on your service
   - Go to "Variables" tab
   - Add these variables:
   
   ```
   SECRET_KEY=your-generated-secret-key
   GOOGLE_CLIENT_ID=your-google-client-id.apps.googleusercontent.com
   GOOGLE_CLIENT_SECRET=GOCSPX-your-google-secret
   PORT=8080
   ```
   
   Generate SECRET_KEY:
   ```bash
   python -c "import secrets; print(secrets.token_urlsafe(32))"
   ```

4. **Configure Build Settings**
   Railway will auto-detect Python and use our configs:
   - `Procfile` - Start command
   - `requirements.txt` - Dependencies
   - `railway.json` - Build configuration
   - `nixpacks.toml` - System dependencies

5. **Deploy**
   - Railway will automatically build and deploy
   - Check logs in "Deployments" tab
   - Wait for "Deployed" status

6. **Get Your URL**
   - Go to "Settings" tab
   - Under "Domains"
   - Click "Generate Domain"
   - Your app will be at: `https://your-app-name.up.railway.app`

#### Option B: Via Railway CLI

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link project
railway link

# Set environment variables
railway variables set SECRET_KEY=your-secret-key
railway variables set GOOGLE_CLIENT_ID=your-client-id
railway variables set GOOGLE_CLIENT_SECRET=your-secret

# Deploy
railway up
```

### 4. Post-Deployment Configuration

#### A. Update Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to your OAuth client
3. Add authorized redirect URI:
   ```
   https://your-app-name.up.railway.app/auth/google/callback
   ```
4. Add authorized JavaScript origin:
   ```
   https://your-app-name.up.railway.app
   ```

#### B. Update Frontend

Update `site/index.qmd` and `site/login.html` with your Google Client ID:
```javascript
const clientId = 'your-actual-client-id.apps.googleusercontent.com';
```

Then rebuild:
```bash
cd site
quarto render
git add .
git commit -m "update: production Google OAuth config"
git push
```

Railway will auto-deploy the update.

### 5. Test Your Deployment

1. **Homepage**
   ```
   https://your-app-name.up.railway.app/
   ```

2. **Login**
   ```
   https://your-app-name.up.railway.app/login.html
   ```

3. **API Docs**
   ```
   https://your-app-name.up.railway.app/docs
   ```

4. **User Dashboard** (after login)
   ```
   https://your-app-name.up.railway.app/user/dashboard
   ```

5. **Dashboards**
   - IT Tenders: `/dashboard/it-tenders`
   - Countries: `/dashboard/countries`
   - Value Analysis: `/dashboard/value-analysis`
   - Awards: `/dashboard/awards`

### 6. Monitor Your App

In Railway dashboard:
- **Metrics** tab - CPU, Memory, Network usage
- **Logs** tab - Application logs
- **Deployments** tab - Deployment history

---

## Features Checklist (All Implemented)

### Data Sources ✅
- [x] TED (EU) - 500,000+ tenders/year
- [x] SAM.gov (US) - 100,000+ opportunities/year
- [x] KIMDIS (Greece) - 30,000+ tenders/year
- [x] Diavgeia (Greece) - 2M+ decisions/year

### Dashboards ✅
- [x] Power BI style tab-based layout
- [x] Minimal scrolling - single screen per tab
- [x] 6 visualization tabs per dashboard
- [x] Real-time KPIs
- [x] Interactive Plotly charts
- [x] Responsive design

### Authentication ✅
- [x] Email/password login
- [x] Email/password signup
- [x] Google OAuth integration
- [x] JWT token authentication
- [x] Protected routes
- [x] Session management

### User Features ✅
- [x] Personal dashboard
- [x] Favorites/bookmarks
- [x] Quick stats
- [x] Recent activity
- [x] Quick actions menu
- [x] User settings (ready)

### API ✅
- [x] Search tenders endpoint
- [x] Statistics endpoint
- [x] Favorites CRUD
- [x] Authentication endpoints
- [x] Swagger documentation
- [x] CORS enabled

### Templates & Analytics ✅
- [x] Dataset type analysis for each source
- [x] Top interim facts defined
- [x] KPI templates
- [x] Chart templates
- [x] Dashboard templates

---

## Troubleshooting

### Build Fails

**Issue:** Quarto not found
**Solution:** Check `nixpacks.toml` has `quarto` in nixPkgs

**Issue:** Python dependencies fail
**Solution:** Check `requirements.txt` syntax

### Runtime Errors

**Issue:** "Site not rendered"
**Solution:** Make sure Quarto render runs in build phase

**Issue:** "Port already in use"
**Solution:** Railway uses PORT env variable automatically

### Google OAuth Not Working

**Issue:** "redirect_uri_mismatch"
**Solution:** Update Google Console with production URL

**Issue:** "invalid_client"
**Solution:** Check environment variables are set correctly

---

## Custom Domain (Optional)

1. Go to Railway project → Settings → Domains
2. Click "Custom Domain"
3. Enter your domain
4. Add DNS records as shown
5. Wait for DNS propagation

---

## Scaling & Performance

Railway auto-scales based on:
- CPU usage
- Memory usage
- Request volume

To upgrade:
1. Go to project Settings
2. Under "Plan", upgrade to Pro
3. Configure auto-scaling limits

---

## Database Migration (Future)

Current: In-memory storage
Recommended: PostgreSQL on Railway

```bash
# Add PostgreSQL
railway add

# Select PostgreSQL
# Railway will provide DATABASE_URL

# Update code to use database
```

---

## Success! 🎉

Your Procurement Intelligence Platform is now live with:

✅ Multi-source government procurement data  
✅ Beautiful Power BI-style dashboards  
✅ User authentication & personal dashboards  
✅ Favorites & bookmarking  
✅ Full REST API  
✅ Google OAuth ready  
✅ Production-grade deployment  

**Share your deployment:**  
`https://your-app-name.up.railway.app`
