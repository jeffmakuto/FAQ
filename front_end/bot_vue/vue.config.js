const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
	devServer: {
		host: '0.0.0.0',
		port: 8080,
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

