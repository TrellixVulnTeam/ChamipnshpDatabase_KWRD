/* eslint-disable no-dupe-keys */
import JWTDecode from 'jwt-decode'
import cookieparser from 'cookieparser'

export const actions = {
  nuxtServerInit({ commit }, { req }) {
    if (process.server && process.static) return
    if (!req.headers.cookie) return

    const parsed = cookieparser.parse(req.headers.cookie)
    const accsessTokenCookie = parsed.access_token

    if (!accsessTokenCookie) return

    const decoded = JWTDecode(accsessTokenCookie)
    if (decoded) {
      commit('users/SET_USER', {
        uid: decoded.user_id,
        email: decoded.email,
      })
    }

    const parsedAdmin = cookieparser.parse(req.headers.cookie)
    const adminTokenCookie = parsedAdmin.admin_token

    if (!adminTokenCookie) {
      commit('users/SET_ADMIN_USER', false)
    } else {
      commit('users/SET_ADMIN_USER', true)
    }
  },
}
