/**
 * Vercel Speed Insights Integration
 * This script loads and initializes Speed Insights for the website
 */
import { injectSpeedInsights } from './node_modules/@vercel/speed-insights/dist/index.mjs';

// Initialize Speed Insights
injectSpeedInsights({
  // Framework is not specified for vanilla JS
  framework: 'html',
  // Auto-detect development/production based on environment
  // In production on Vercel, this will use the optimized script
});
