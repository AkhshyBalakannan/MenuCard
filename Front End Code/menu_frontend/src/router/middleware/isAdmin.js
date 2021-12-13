export default function isAdmin({ next, store }) {
    if (!store.getters.auth.isSubscribed) {
        return next({
            name: 'menucard'
        })
    }

    return next()
}