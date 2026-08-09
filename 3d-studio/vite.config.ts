/// <reference types="vitest/config" />
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base is architecturally fixed: the app is served from mrbadmus.com/3d, and the
// Stage 9 publication step copies 3d-studio/dist/ to mrbadmus_site/3d/ (MRB-194).
export default defineConfig({
  base: '/3d/',
  plugins: [react()],
  server: { port: 8899, strictPort: true },
  preview: { port: 8899, strictPort: true },
  test: {
    environment: 'jsdom',
    setupFiles: ['tests/setup.ts'],
    include: ['tests/**/*.test.{ts,tsx}'],
    testTimeout: 20000,
  },
})
