#ifndef _PULSAR_LUA_EXTRA_H_
#define _PULSAR_LUA_EXTRA_H_

#include "lualib.h"
#include "lauxlib.h"


#ifdef _MSC_VER
#include <stdlib.h>
#include <math.h>
#define STIN static __inline
#define EXIN extern __inline
#define snprintf _snprintf
#define isnan(x) _isnan(x)
#define isinf(x) (!_finite(x))
#define strncasecmp _strnicmp
#else
#define STIN static inline
#define EXIN extern inline
#endif

#endif  //  _PULSAR_LUA_EXTRA_H_
