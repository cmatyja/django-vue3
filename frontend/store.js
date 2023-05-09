import { reactive } from "vue";

export default (store = reactive({
	token: null,
	setToken(token) {
		this.token = token;
	},

	count: 0,

	increment(event) {
		this.count++;
		console.log(event);
	},
}));
