const path = require("path")

module.exports = {
    entry: "./src/app.js",
    output: {
        filename: "bundle.js",
        path: path.join(__dirname, "public")
    },
    module: {
        rules: [{
            loader: "babel-loader",
            test: /\.js$/,
            exclude: /node_modules/
        }]
    },
    devServer: {
        static: path.join(__dirname, "public"),
        port: 9000
    },
    mode: "development"
}