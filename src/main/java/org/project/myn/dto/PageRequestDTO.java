package org.project.myn.dto;

@Builder
@AllArgsConstructor
@Data
public class PageRequestDTO {

    // 페이지
    private int page;
    private int size;
    // 검색
    private String type;
    private String keyword;

    public PageRequestDTO() {
        this.page = 1;
        this.size = 10;
    }

    public Pageable getPageable(Sort sort) {
        return PageRequest.of(page - 1, size, sort);
    }

}

