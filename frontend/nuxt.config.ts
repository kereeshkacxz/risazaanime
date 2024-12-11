// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: false },

  css: ["~/assets/css/main.css"],

  vite: {
    server: {
      watch: {
        usePolling: true,
      },
    },
  },

  app: {
    head: {
      title: "RZA",
      meta: [
        {
          name: "description",
          content: "anime review site",
        },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
        { name: "keywords", content: "nuxt, vue, app, web-development" },
      ],
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Yuji+Mai&display=swap",
        },
        {
          rel: "icon",
          type: "image/x-icon",
          href: "/favicon.ico",
        },
      ],
    },
  },

  runtimeConfig: {
    public: {
      backendUrl: "http://localhost:8000",
      pages: {},
    },
  },

  components: [
    {
      path: "~/components",
      pathPrefix: false,
    },
  ],

  compatibilityDate: "2024-08-14",
  modules: ["@nuxt/image"],
  image: { dir: "public" },
});
