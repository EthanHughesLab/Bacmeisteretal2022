#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;
#if defined(__cplusplus)
extern "C" {
#endif

extern void _km_reg(void);
extern void _kv_reg(void);
extern void _nav12_reg(void);
extern void _nav16_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," \"km.mod\"");
    fprintf(stderr," \"kv.mod\"");
    fprintf(stderr," \"nav12.mod\"");
    fprintf(stderr," \"nav16.mod\"");
    fprintf(stderr, "\n");
  }
  _km_reg();
  _kv_reg();
  _nav12_reg();
  _nav16_reg();
}

#if defined(__cplusplus)
}
#endif
