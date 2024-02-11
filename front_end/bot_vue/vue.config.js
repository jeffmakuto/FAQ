const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
	devServer: {
		host: '0.0.0.0',
		port: 8080,
		https: true,
		key: path.resolve(__dirname, 'key.pem'),
		cert: path.resolve(__dirname, 'cert.pem'),
	},
	transpileDependencies: true,
	chainWebpack: (config) => {
		config.plugin('define').tap((args) => {
			const defineArgs = args[0];

			/* Add or modify the feature flags here */
			defineArgs['__VUE_OPTIONS_API__'] = true;
			defineArgs['__VUE_PROD_DEVTOOLS__'] = false;
			defineArgs['__VUE_PROD_HYDRATION_MISMATCH_DETAILS__'] = false;
			return args;
		});
	},
});

