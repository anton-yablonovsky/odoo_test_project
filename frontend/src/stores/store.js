import { defineStore } from 'pinia'

export const useStore = defineStore('store', {
    state: () => {
        return {
            isAuthenticatedState: false,
            userRole: "",
            buildings: [],
            entrances: [],
            apartments: [],
            users: [],
            manager_buildings: [],
            guard_entrances: [],
            inhabitant_apartments: [],
        }
    },
    actions: {
        async setCsrfToken() {
            await fetch('http://localhost:8000/backend/api/set_csrf_token/', {
                method: 'GET',
                credentials: 'include'
            })
        },

        async login(username, password) {
            const response = await fetch('http://localhost:8000/backend/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken()
                },
                body: JSON.stringify({ username, password }),
                credentials: 'include'
            })
            const data = await response.json()
            if (data.success) {
                this.isAuthenticatedState = true
                this.saveState()
            } else {
                this.isAuthenticatedState = false
                this.saveState()
            }
        },

        async logout() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/logout', {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCSRFToken()
                    },
                    credentials: 'include'
                })
                if (responsisAuthenticatede.ok) {
                    this.isAuthenticatedState = false
                    this.saveState()
                }
            } catch (error) {
                console.error('Logout failed', error)
                throw error
            }
        },

        async isAuthenticated() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/user/is_authenticated/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })
                if (response.ok) {
                    const data = await response.json()
                    this.isAuthenticatedState = true
                }
                else {
                    this.isAuthenticatedState = false
                }
            } catch (error) {
                console.error('Failed to fetch user', error)
                this.isAuthenticatedState = false
            }
            this.saveState()
        },

        async getUserRole() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/get_user_role/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })

                if (response.ok) {
                    const data = await response.json()
                    this.userRole = data.role;
                }
                else {
                    alert('Role issue!');
                }
            } catch (error) {
                console.error('Failed to get user role', error)
            }
            this.saveState()
        },

        async getBuildings() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/get_buildings_list/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })

                if (response.ok) {
                    const data = await response.json()
                    console.log("buildings");
                    console.log(data);
                    this.buildings = data;
                }
                else {
                    alert('Buildings issue!');
                }
            } catch (error) {
                console.error('Failed to get buildings', error)
            }
            this.saveState()
        },


        async getEntrances() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/get_entrances_list/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })

                if (response.ok) {
                    const data = await response.json()
                    console.log("entrances");
                    console.log(data);
                    this.entrances = data;
                }
                else {
                    alert('Entrances issue!');
                }
            } catch (error) {
                console.error('Failed to get entrances', error)
            }
            this.saveState()
        },


        async getApartments() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/get_apartments_list/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })

                if (response.ok) {
                    const data = await response.json()
                    console.log("apartments");
                    console.log(data);
                    this.apartments = data;
                }
                else {
                    alert('Apartments issue!');
                }
            } catch (error) {
                console.error('Failed to get apartments', error)
            }
            this.saveState()
        },

        async getUsers() {
            try {
                const response = await fetch('http://localhost:8000/backend/api/get_users_list/', {
                    credentials: 'include',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                })

                if (response.ok) {
                    const data = await response.json()
                    console.log("users");
                    console.log(data);
                    this.users = data;
                }
                else {
                    alert('Users issue!');
                }
            } catch (error) {
                console.error('Failed to get users', error)
            }
            this.saveState()
        },

        async getManagerBuildings() {
            try {
              const response = await fetch('http://localhost:8000/backend/api/manager_buildings/', {
                  credentials: 'include',
                  headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCSRFToken()
                  },
              })
      
              if (response.ok) {
                  const data = await response.json()
                  this.manager_buildings = data;
              }
              else {
                  alert('Manager buildings issue!');
              }
              } catch (error) {
                  console.error('Failed to get manager buildings', error)
              }
          },

          async getGuardEntrances() {
            try {
              const response = await fetch('http://localhost:8000/backend/api/guard_entrances/', {
                  credentials: 'include',
                  headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCSRFToken()
                  },
              })
      
              if (response.ok) {
                  const data = await response.json()
                  console.log("data");
                  console.log(data);
                  this.guard_entrances = data;

              }
              else {
                  alert('Guard entrances issue!');
              }
              } catch (error) {
                  console.error('Failed to get guard entrances', error)
              }
          },

          async getInhabitantApartments() {
            try {
              const response = await fetch('http://localhost:8000/backend/api/inhabitant_apartments/', {
                  credentials: 'include',
                  headers: {
                      'Content-Type': 'application/json',
                      'X-CSRFToken': getCSRFToken()
                  },
              })
      
              if (response.ok) {
                  const data = await response.json()
                  this.inhabitant_apartments = data;
              }
              else {
                  alert('Inhabitant apartments issue!');
              }
              } catch (error) {
                  console.error('Failed to get inhabitant apartments', error)
              }
          },

        saveState() {
            localStorage.setItem('storeState', JSON.stringify({
                isAuthenticatedState: this.isAuthenticatedState
            }))
        }
    }
})

export function getCSRFToken() {
    /*
    We get the CSRF token from the cookie to include in our requests.
    This is necessary for CSRF protection in Django.
     */
    const name = 'csrftoken';
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    if (cookieValue === null) {
        throw 'Missing CSRF cookie.'
    }
    return cookieValue;
}

