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
        }
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
        }
    },

    mutations: {
        troggle_on_auth: (state) => {
            state.user.loggedIn = true;
        },
        troggle_off_auth: (state) => {
            state.user.loggedIn = false;
        }
    },

    actions: {
        troggle_on_auth: (context) => {
            setTimeout(function () { // reach out for data
                context.commit('troggle_on_auth');
            }, 0);
        },
        troggle_off_auth: (context) => {
            setTimeout(function () { // reach out for data
                context.commit('troggle_off_auth');
            }, 0);
        }
    }
})
