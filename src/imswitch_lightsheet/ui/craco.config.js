const { ModuleFederationPlugin } = require("webpack").container;
const deps = require("./package.json").dependencies;

module.exports = {
  webpack: {
    configure: (config) => {
      // let webpack pick a correct publicPath at runtime
      config.output.publicPath = "auto";

      config.plugins.push(
        new ModuleFederationPlugin({
          name: "lightsheet_plugin",          // must match UIExport.scope
          filename: "remoteEntry.js",
          exposes: {
            "./Widget": "./src/Widget",       // must match UIExport.exposed
          },
          shared: {
            react:               { singleton: true, requiredVersion: false },
            "react-dom":         { singleton: true, requiredVersion: false },
            "react-dom/client":  { singleton: true, requiredVersion: false },
            "react/jsx-runtime": { singleton: true, requiredVersion: false },
          },
        })
      );

      return config;
    },
  },
};
