Montagu Stasie — static site

This folder contains a simple static site. The root `index.html` is the landing page and links into `main.html` (the main site).

Quick deploy with Vercel (recommended)

1. Install Vercel CLI (requires Node/npm):

```powershell
npm install -g vercel
```

2. From PowerShell in the project folder:

```powershell
cd 'C:\Users\ACER\Desktop\Montagu-Stasie-Website'
vercel login
vercel
```

Follow the prompts. When asked for the root directory, choose the current folder. Vercel will detect a static site and deploy.

Add a custom domain

- In the Vercel dashboard, open your project → Domains → Add.
- Or via CLI:

```powershell
vercel domains add yourdomain.com
```

Vercel will provide DNS records (A, CNAME). Add those records at your registrar and wait for DNS propagation.

Notes

- If you want the landing page to be `main.html` instead, you can rename files accordingly. Currently `index.html` is the landing page and it links to `main.html`.
- To enable automatic deploys from Git, push this folder to GitHub and connect the repo in the Vercel dashboard.

If you want, I can:
- Deploy now and open the deployed URL in your browser.
- Configure redirects or rename files differently.
