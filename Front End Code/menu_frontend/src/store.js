import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';
import Cookies from 'js-cookie';
import SecureLS from "secure-ls";
var ls = new SecureLS({ isCompression: false });

Vue.use(Vuex)


export default new Vuex.Store({
    state: {
        user: {
            loggedIn: false,
            isAdmin: false
        },
        url: 'http://localhost:5000',
        token: ''
    },
    // below block of code is simple cookie based storage with secure false
    // plugins: [createPersistedState({
    //   storage: {
    //     getItem: key => Cookies.get(key),
    //     setItem: (key, value) => Cookies.set(key, value, { expires: 3, secure: true }),
    //     removeItem: key => Cookies.remove(key)
    //   }
    // })],

    // below block of code is local storage based storage with secure true
    plugins: [
        createPersistedState({
            storage: {
                getItem: (key) => ls.get(key),
                setItem: (key, value) => ls.set(key, value),
                removeItem: (key) => ls.remove(key),
            },
        }),
    ],

    getters: {
        auth(state) {
            return state.user
        },
        admin(state) {
            return state.isAdmin
        },
        url(state) {
            return state.url
        },
        token(state) {
            return state.token
        }
    },

    mutations: {
        troggle_on_auth: (state) => {
            state.user.loggedIn = true;
        },
        troggle_off_auth: (state) => {
            state.user.loggedIn = false;
        },
        troggle_on_admin: (state) => {
            state.user.isAdmin = true;
        },
        troggle_off_admin: (state) => {
            state.user.isAdmin = false;
        },
        set_token: (state, token) => {
            state.token = token
        },
        delete_token: (state) => {
            state.token = ''
        }
    },

    actions: {
        troggle_on_auth: (context) => {
            setTimeout(function () { // reach out for data
                context.commit('troggle_on_auth');
            }, 0);
        },
        troggle_off_auth: (context) => {
            context.commit('troggle_off_auth');
        },
        troggle_on_admin: (context) => {
            setTimeout(function () { // reach out for data
                context.commit('troggle_on_admin');
            }, 0);
        },
        troggle_off_admin: (context) => {
            context.commit('troggle_off_admin');
        },
        set_token: (context, token) => {
            context.commit("set_token", token)
        },
        delete_token: (context) => {
            context.commit("delete_token")
        }
    }
})
